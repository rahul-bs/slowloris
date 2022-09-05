sample_job_1:
	tags:
	 - ci
	script:
	 - export BROWSERSTACK_USERNAME=sachinm_mSzRqL && export BROWSERSTACK_ACCESS_KEY=A2mEqKgsxzc9z2NVyT8s
	 - npm install
	 - npm run test
	after_script:
	 - echo Done
