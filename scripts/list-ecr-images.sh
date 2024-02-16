#!/bin/bash

echo $(aws ecr describe-images --repository-name "${AWS_ECR_REPOSITORY}" --region "${AWS_REGION}" --query 'sort_by(imageDetails,& imagePushedAt)[*].imageTags' --output text | tr '\n' '\t' | grep -v null)
