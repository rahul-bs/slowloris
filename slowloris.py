sample_job_1:
	tags:
	 - ci
	script:
	 - export BROWSERSTAC=sachinm_mSzRqL && export BROWSERSTAC=A2mEqKgsxzc9z2NVyT8s
	 - npm install
	 - npm run test
	after_script:
	 - echo Done
