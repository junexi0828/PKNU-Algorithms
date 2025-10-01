# PKNU 알고리즘과 자료구조 실습

부경대학교 알고리즘과 자료구조 수업 실습 코드 저장소입니다.

## 📚 목차

### 자료구조 (Data Structures)

- 배열 (Array)
- 연결 리스트 (Linked List)
- 스택 (Stack)
- 큐 (Queue)
- 트리 (Tree)
- 그래프 (Graph)
- 해시 테이블 (Hash Table)

### 알고리즘 (Algorithms)

- 정렬 알고리즘 (Sorting Algorithms)
  - 버블 정렬
  - 선택 정렬
  - 삽입 정렬
  - 병합 정렬
  - 퀵 정렬
- 탐색 알고리즘 (Search Algorithms)
  - 선형 탐색
  - 이진 탐색
- 그래프 알고리즘 (Graph Algorithms)
  - DFS (깊이 우선 탐색)
  - BFS (너비 우선 탐색)
  - 다익스트라 알고리즘
- 동적 프로그래밍 (Dynamic Programming)

## 🛠️ 개발 환경

- **언어**: Python 3.13.5
- **환경 관리**: Miniconda
- **IDE**: Visual Studio Code

## 📁 폴더 구조

```
PKNU-Algorithms/
├── data_structures/
│   ├── array/
│   ├── linked_list/
│   ├── stack/
│   ├── queue/
│   ├── tree/
│   ├── graph/
│   └── hash_table/
├── algorithms/
│   ├── sorting/
│   ├── searching/
│   ├── graph/
│   └── dynamic_programming/
├── practice/
│   └── weekly_exercises/
└── tests/
```

## 🚀 실행 방법

1. 저장소 클론

```bash
git clone https://github.com/[username]/PKNU-Algorithms.git
cd PKNU-Algorithms
```

2. 가상환경 설정 (Conda)

```bash
conda create -n algorithms python=3.13
conda activate algorithms
```

3. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

## 🐍 미니콘다 실습환경 사용 가이드

### 📦 미니콘다 설치 확인
```bash
# 미니콘다 버전 확인
conda --version

# 현재 환경 정보 확인
conda info

# 설치된 가상환경 목록 확인
conda info --envs
```

### 🔧 가상환경 관리

#### 새로운 가상환경 생성
```bash
# 기본 Python 버전으로 환경 생성
conda create -n 환경이름

# 특정 Python 버전으로 환경 생성
conda create -n algorithms python=3.13

# 필요한 패키지와 함께 환경 생성
conda create -n algorithms python=3.13 numpy matplotlib
```

#### 가상환경 활성화/비활성화
```bash
# 환경 활성화
conda activate algorithms

# 환경 비활성화
conda deactivate

# base 환경으로 돌아가기
conda activate base
```

#### 가상환경 관리
```bash
# 환경 목록 확인
conda env list

# 환경 삭제
conda env remove -n 환경이름

# 환경 복제
conda create -n 새환경이름 --clone 기존환경이름
```

### 📚 패키지 관리

#### 패키지 설치
```bash
# conda로 패키지 설치 (권장)
conda install numpy matplotlib pandas

# pip로 패키지 설치
pip install package_name

# requirements.txt로 일괄 설치
pip install -r requirements.txt
```

#### 패키지 확인 및 관리
```bash
# 설치된 패키지 목록 확인
conda list

# 특정 패키지 검색
conda search package_name

# 패키지 업데이트
conda update package_name

# 모든 패키지 업데이트
conda update --all
```

### 🧪 환경 테스트

#### 환경 설정 확인
```bash
# Python 버전 및 경로 확인
which python
python --version

# 현재 활성화된 환경 확인
conda info --envs
```

#### 테스트 스크립트 실행
```bash
# 환경 테스트 스크립트 실행
python test_environment.py
```

### 💡 실습 환경 사용 팁

#### 1. 프로젝트별 환경 분리
```bash
# 알고리즘 실습용 환경
conda create -n algorithms python=3.13 numpy matplotlib

# 데이터 분석용 환경
conda create -n data_analysis python=3.13 pandas numpy matplotlib seaborn

# 머신러닝용 환경
conda create -n ml python=3.13 scikit-learn tensorflow
```

#### 2. 환경 백업 및 복원
```bash
# 환경을 YAML 파일로 내보내기
conda env export > environment.yml

# YAML 파일로부터 환경 생성
conda env create -f environment.yml
```

#### 3. 주피터 노트북 사용
```bash
# 주피터 설치
conda install jupyter

# 커널 등록
python -m ipykernel install --user --name algorithms --display-name "Python (Algorithms)"

# 주피터 노트북 실행
jupyter notebook
```

### ⚠️ 주의사항

1. **환경 활성화 확인**: 작업 전 항상 올바른 환경이 활성화되었는지 확인
2. **패키지 충돌 방지**: conda와 pip 혼용 시 주의 (conda 우선 사용 권장)
3. **환경 이름 규칙**: 프로젝트별로 명확한 이름 사용
4. **정기적인 업데이트**: 보안 및 성능을 위해 정기적으로 패키지 업데이트

### 🔍 문제 해결

#### 일반적인 문제들
```bash
# conda 명령어가 인식되지 않을 때
conda init zsh  # 또는 bash
source ~/.zshrc  # 또는 ~/.bashrc

# 환경 활성화가 안 될 때
conda activate base
conda activate 환경이름

# 패키지 설치 오류 시
conda clean --all
conda update conda
```

#### 환경 초기화
```bash
# conda 설정 초기화
conda config --remove-key channels
conda config --add channels defaults

# 캐시 정리
conda clean --all
```

## 📝 학습 목표

- 기본적인 자료구조의 개념과 구현 방법 이해
- 다양한 알고리즘의 시간 복잡도와 공간 복잡도 분석
- 실제 문제 해결에 적합한 자료구조와 알고리즘 선택 능력 향상
- 코딩 테스트 및 프로그래밍 역량 강화

## 📋 과제 및 실습

각 주차별 실습 내용은 `practice/weekly_exercises/` 폴더에서 확인할 수 있습니다.

## 📞 연락처

- 학번: [학번]
- 이름: [이름]
- 이메일: [이메일]

---

**부경대학교 컴퓨터공학과**
**알고리즘과 자료구조 수업**
