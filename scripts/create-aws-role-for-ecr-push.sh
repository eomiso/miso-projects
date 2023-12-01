#!/bin/bash

# Get role name, git org or user, and git repo
# If not set, error out later
# @TODO: add help text
# @TODO: verify org/repo are not wildcards

while getopts ":r:o:g:h:p:" opt; do
  case $opt in
    r) ROLE_NAME="$OPTARG"
    ;;
    o) GIT_ORG="$OPTARG"
    ;;
    g) GIT_REPO="$OPTARG"
    ;;
    p) IMG_PREFIX="$OPTARG"
    ;;
    h) echo "Usage: $0 -r <role name> -o <git org or user> -g <git repo> -p <image prefix>"
    ;;
    :)
    echo "$0: Must supply an argument to -$OPTARG." >&2
    exit 1
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done
# Check if required options are set
if [ -z "$ROLE_NAME" ]; then
    echo "Must supply a role name with -r"
    exit 1
fi
if [ -z "$GIT_ORG" ]; then
    echo "Must supply a git org or user with -o"
    exit 1
fi
if [ -z "$GIT_REPO" ]; then
    echo "Must supply a git repo with -g"
    exit 1
fi

# check if aws cli is installed
which aws > /dev/null
if [ $? -ne 0 ]; then
    echo "aws cli is not installed"
    exit 1
fi

# Prerequisites are met, continue with script

# get aws account id and check credentials are active
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
if [ -z "$AWS_ACCOUNT_ID" ]; then
    echo "AWS account ID not found -- do you have AWS credentials configured?"
    exit 1
fi


echo "Create and attach a policy to ${ROLE_NAME} that allows it to do whatever your heart desires"

# ecr:GetAuthorizationToken Works wonly when resource is *
ARPO_FILE=$(mktemp)
cat<<EOF>"${ARPO_FILE}"
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "WriteImage",
			"Effect": "Allow",
			"Action": [
                "ecr:CompleteLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:InitiateLayerUpload",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage"
			],
			"Resource": "arn:aws:ecr:ap-northeast-2:226685225888:repository/${IMG_PREFIX}-${GIT_REPO}"
		},
        {
			"Sid": "ReadAndDeleteImage",
			"Effect": "Allow",
			"Action": [
				"ecr:DescribeImages",
				"ecr:BatchDeleteImage"
			],
			"Resource": "arn:aws:ecr:ap-northeast-2:226685225888:repository/${IMG_PREFIX}-${GIT_REPO}"
        },
		{
			"Sid": "AuthOnly",
			"Effect": "Allow",
			"Action": [
				"ecr:GetAuthorizationToken"
			],
			"Resource": [
				"*"
			]
		}
	]
}
EOF

function kebabToPascalCase() {
    local input="$1"
    local output=""

    # Capitalize the first letter
    output=$(tr '[:lower:]' '[:upper:]' <<< "${input:0:1}")

    # Process the rest of the string
    for ((i = 2; i <= ${#input}; i++)); do
        char="${input:i-1:1}"
        if [ "$char" == "-" ]; then
            # Skip hyphen and capitalize the next letter
            output+=$(tr '[:lower:]' '[:upper:]' <<< "${input:i:1}")
            ((i++))
        else
            # Keep the character as is
            output+="$char"
        fi
    done

    echo "$output"
}


POLICY_NAME="${GIT_ORG}$(kebabToPascalCase "${GIT_REPO}")ImageECRPushPolicy"

aws iam create-policy \
  --policy-name "${POLICY_NAME}" \
  --policy-document "file://${ARPO_FILE}"

aws iam attach-role-policy \
    --policy-arn "arn:aws:iam::${AWS_ACCOUNT_ID}:policy/${POLICY_NAME}" \
    --role-name "${ROLE_NAME}"
