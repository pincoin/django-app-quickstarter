setuptools setup.py 파일 옵션 설명

# `install_requires`

프로젝트에 필요한 패키지를 지정한다. 패키지 이름의 대소문자는 중요하지 않다.

# `setup_requires`

`install_requires` 옵션은 프로젝트에 필요한 패키지 목록이고 `setup.py` 파일 자신을 위해 필요한 패키지가 있을 수 있는데 이를 지정한다.

# `scripts`

프로젝트 설치할 때 같이 설치되는 스크립트 파일을 지정한다. 예를 들어, Django 프로젝트는 manage.py 파일을 같이 배포하고 있다.
여기에 지정한 스크립트는 가상환경의 bin 디렉터리에 설치되어 어느 곳에서든 실행 가능하다.

# `tests_require`

테스트 실행을 위해 추가적으로 필요한 패키지 목록이다.

# `test_suite`

테스트 시 실행할 도구이다.

# `zip_safe`

zip 파일로 만들어서 실행해도 패키지가 정상적으로 동작하는지 여부이다.
