#!/bin/bash

while getopts ":r:o:h:" opt; do
  case $opt in
    r) ROLE_NAME="$OPTARG"
    ;;
    o) GIT_ORG="$OPTARG"
    ;;
    h) echo "Usage: $0 -r <role name> -o <git org or user> -g <git repo>"
    ;;
    :)
    echo "$0: Must supply an argument to -$OPTARG." >&2
    exit 1
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

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

echo "Creating an OpenID Connect provider for GitHub Actions in AWS account ${AWS_ACCOUNT_ID}"
# The thumbprint is required to create the OIDC provider when done via CLI, but will be ignored by AWS for GitHub Actions
aws iam create-open-id-connect-provider \
    --url https://token.actions.githubusercontent.com \
    --thumbprint-list 1b511abead59c6ce207077c0bf0e0043b1382612 \
    --client-id-list sts.amazonaws.com \

# Build trust policy specifying the org/repo
# This could be further restricted by replacing the wildcard with a particular environment and branch
ARPD_FILE=$(mktemp)
cat<<EOF>"${ARPD_FILE}"
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::226685225888:oidc-provider/token.actions.githubusercontent.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringLike": {
                    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
                    "token.actions.githubusercontent.com:sub": "repo:eomiso/sample-api:main"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::226685225888:user/SampleApiCiAgent"
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession"
            ]
        }
    ]
}
EOF
echo "Creating IAM role ${ROLE_NAME} with trust policy allowing GitHub Actions to assume it"
echo "Only actions stemming from the ${GIT_ORG} organization will be allowed to assume this role"
aws iam create-role \
    --role-name "$ROLE_NAME" \
    --assume-role-policy-document "file://${ARPD_FILE}"
