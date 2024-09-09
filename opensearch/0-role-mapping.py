import boto3
import requests

# AWS 자격 증명 설정
service = 'es'

# 현재 리전
region = 'us-west-2' # e.g. us-west-1

# 아래 등록하신 Admin  아이디와 비밀번호를 입력합니다.
# IAM credential 로 하면 안됩니다.
awsauth = ('ADMIN_ID', 'ADMIN_PASSWORD') 

# 기존 사용하시던 OpenSearch 도메인 엔드포인트입니다.
host = 'OPENSEARCH_DOMAIN_ENDPOINT'

# manage_snapshots 역할에 매핑할 IAM 역할 ARN
# SageMaker Notebook 에 연결되어 있는 Role 을 입력합니다.
iam_role_arn = 'IAM ROLE ARN OF CALLER'

# 역할 매핑 API 엔드포인트
path = '/_plugins/_security/api/rolesmapping/manage_snapshots'
url = host + path

# 역할 매핑 요청 본문
payload = {
    "backend_roles": [iam_role_arn],
    "hosts": [],
    "users": []
}

# PUT 요청 보내기
headers = {"Content-Type": "application/json"}
r = requests.put(url, auth=awsauth, json=payload, headers=headers)

# 응답 확인
print(r.status_code)
print(r.text)
