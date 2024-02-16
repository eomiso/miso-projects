const core = require('@actions/core');
import { App } from "octokit";

try {
  const APP_ID = core.getInput('gh-app-id');
  const PRIVATE_KEY_BASE64 = core.getInput('gh-app-private-key-base64');
  const PRIVATE_KEY = Buffer.from(PRIVATE_KEY_BASE64, 'base64').toString('utf-8');
  const IMAGE_NAME = core.getInput('image-name');
  const TAG = core.getInput('tag');
  const MANIFEST_PATH = core.getInput('manifest-path');
  const NAMESPACE = core.getInput('namespace') || null;

  const ORG = core.getInput('organization') || 'zaikorea';
  const REPO = core.getInput('repository');


  console.log({ APP_ID, PRIVATE_KEY, IMAGE_NAME, TAG, MANIFEST_PATH, NAMESPACE, ORG, REPO });

  const app = new App({
    appId: APP_ID,
    privateKey: PRIVATE_KEY,
  });

  for await (const { octokit, repository } of app.eachRepository.iterator()) {
    const { data } = await octokit.request(`GET /repos/{owner}/{repo}`, {
      owner: repository.owner.login,
      repo: repository.name,
    });
    console.log(data);

    const { data: }
  }


} catch (error) {
  core.setFailed(error.message);
}
