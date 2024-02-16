import base64
import logging
import os

import jwt
from github import Auth, Github, GithubIntegration

LOG = logging.getLogger(__name__)
LOG.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

ECR_REGISTRY = "226685225888.dkr.ecr.ap-northeast-2.amazonaws.com"
CLIENT_SECRET = "d7afe97a243a380cd9035fe3ae82e5cd7f4f7a01"

app_id = 667317
app_key = """
-----BEGIN RSA PRIVATE KEY-----
{{ content-should-be-in-your-local }}
-----END RSA PRIVATE KEY-----
"""

# with open(
#         os.path.normpath(os.path.expanduser('~/.certs/github/eomiso-cicd-agent.2023-12-02.private-key.pem')),
#         'r'
# ) as cert_file:
#     app_key = cert_file.read()


def get_credential():
    client_secret = CLIENT_SECRET
    return client_secret


GITHUB_ACCESS_TOKEN = get_credential()
git_integration = GithubIntegration(
    auth=Auth.AppAuth(app_id=667317, private_key=app_key)
)
git_installation_id = git_integration.get_repo_installation(
    "eomiso", "k8s-manifests"
).id
print(git_installation_id)
token = git_integration.get_access_token(git_installation_id).token
print(token)

GITHUB_CLIENT = Github(login_or_token=token)
# GITHUB_CLIENT = Github(auth=Auth.Login("Iv1.9faab950713c64fc", CLIENT_SECRET))


def update_k8s_groundtruth_image_tag():
    git_integration = GithubIntegration(
        auth=Auth.AppAuth(app_id=667317, private_key=app_key)
    )

    def _update_files_in(target_dir_path: str):
        target_dir = gh_repo.get_contents(target_dir_path)

        for target_file in target_dir:
            if target_file.type == "dir":
                _update_files_in(target_file.path)
            elif target_file.type == "file":
                decoded_lines = (
                    base64.b64decode(target_file.content).decode("utf-8").split("\n")
                )

                lines = []
                updated = False
                for line in decoded_lines:
                    if f"image: {ECR_REGISTRY}/{ecr_repo}:" in line:
                        old_image_tag = line.split(":")[-1].split(" ")[0].strip()
                        line = line.replace(f":{old_image_tag}", f":{image_tag}")
                        updated = old_image_tag != image_tag

                    lines.append(line)

                if updated:
                    gh_repo.update_file(
                        target_file.path,
                        f"Automated commit by ECR push ({ecr_repo}:{old_image_tag} ➡️ {image_tag})",
                        "\n".join(lines),
                        target_file.sha,
                    )

    try:
        ecr_repo = "eomiso-sample-api"
        image_tag = "latest"

        gh_repo = GITHUB_CLIENT.get_repo("eomiso/k8s-manifests")
        _update_files_in(f".")

        return "SUCCESS"
    except:
        LOG.exception("Lambda function failed:")
        return "ERROR"


if __name__ == "__main__":
    update_k8s_groundtruth_image_tag()
