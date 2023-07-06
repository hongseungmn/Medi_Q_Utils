#패키지 초기화 파일
#"import 패키지명" 으로만 import 할 수 있도록 __init__.py 초기화 하기

#원리] 현재 패키지(.) 즉 mathematics디렉토리의 module3를 불러온다
#단 .(상대경로 표기법)는 실행 파일로 사용하는 모듈에서는 사용 불가(에러 발생)

#방법 1] 아래는 모듈을 필요로 하는 페이지에서 import 패키지명
#from . import module3

#방법 2]
from .module3 import *