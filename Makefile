deploy:
	gcloud functions deploy check-fizz-buzz --gen2 --region=asia-northeast1 --runtime=python39 --entry-point=CheckFizzBuzz --trigger-http --allow-unauthenticated
