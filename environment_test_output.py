#!/usr/bin/env python3
"""
PKNU 알고리즘과 자료구조 실습 - 환경 테스트 출력 프로그램
test_environment.py의 요구사항을 그대로 출력하는 프로그램
"""

import sys
import platform
from datetime import datetime


def test_python_environment():
    """Python 환경 정보를 출력하고 기본 기능을 테스트합니다."""

    print("=" * 60)
    print("🐍 PKNU 알고리즘과 자료구조 실습 - 환경 테스트")
    print("=" * 60)

    # 1. Python 버전 정보
    print(f"📍 Python 버전: {sys.version}")
    print(f"📍 Python 실행 경로: {sys.executable}")
    print(f"📍 플랫폼: {platform.platform()}")
    print(f"📍 아키텍처: {platform.architecture()}")
    print(f"📍 현재 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 2. 기본 자료구조 테스트
    print("🔍 기본 자료구조 테스트:")

    # 리스트 테스트
    test_list = [1, 2, 3, 4, 5]
    print(f"   ✅ 리스트: {test_list}")

    # 딕셔너리 테스트
    test_dict = {"name": "PKNU", "subject": "알고리즘", "year": 2025}
    print(f"   ✅ 딕셔너리: {test_dict}")

    # 집합 테스트
    test_set = {1, 2, 3, 4, 5}
    print(f"   ✅ 집합: {test_set}")

    # 튜플 테스트
    test_tuple = (10, 20, 30)
    print(f"   ✅ 튜플: {test_tuple}")
    print()

    # 3. 간단한 알고리즘 테스트
    print("🧮 간단한 알고리즘 테스트:")

    # 버블 정렬 구현
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    # 정렬 테스트
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(unsorted_list.copy())
    print(f"   📥 정렬 전: {unsorted_list}")
    print(f"   📤 정렬 후: {sorted_list}")

    # 이진 탐색 구현
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # 탐색 테스트
    target = 25
    index = binary_search(sorted_list, target)
    print(f"   🔍 {target} 탐색 결과: 인덱스 {index}")
    print()

    # 4. 수학 연산 테스트
    print("🔢 수학 연산 테스트:")

    # 피보나치 수열
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    fib_numbers = [fibonacci(i) for i in range(10)]
    print(f"   📊 피보나치 수열 (0-9): {fib_numbers}")

    # 팩토리얼
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    print(f"   📊 5! = {factorial(5)}")
    print()

    # 5. 모듈 import 테스트
    print("📦 모듈 import 테스트:")

    try:
        import math

        print(f"   ✅ math 모듈: π = {math.pi:.6f}")

        import random

        random_numbers = [random.randint(1, 100) for _ in range(5)]
        print(f"   ✅ random 모듈: {random_numbers}")

        import os

        print(f"   ✅ os 모듈: 현재 디렉토리 = {os.getcwd()}")

    except ImportError as e:
        print(f"   ❌ 모듈 import 오류: {e}")

    print()

    # 6. Python 출력 포매팅 테스트
    print("🖨️ Python 출력 포매팅 테스트:")
    print("   프린트 문은 기본적인 출력 이외에 출력의 양식을 형식을 지정 가능")
    print()

    # (1) % string 포매팅
    print("   📝 (1) % string 포매팅:")
    print(f"      print(1,2,3) → ", end="")
    print(1, 2, 3)

    print(f'      print("a" + " " + "b" + " " + "c") → ', end="")
    print("a" + " " + "b" + " " + "c")

    print(f'      print("%d %d %d" % (1,2,3)) → ', end="")
    print("%d %d %d" % (1, 2, 3))
    print()

    # (2) format 함수
    print("   📝 (2) format 함수:")
    print('      print("{} {} {}".format("a","b","c")) → ', end="")
    print("{} {} {}".format("a", "b", "c"))
    print()

    # (3) f-string
    print("   📝 (3) f-string:")
    value = "5"
    print(f'      print(f"value is {{value}}") → ', end="")
    print(f"value is {value}")
    print()

    # 추가 포매팅 예제들
    print("   🔧 추가 포매팅 예제:")

    # 숫자 포매팅
    number = 3.14159
    print(f"      소수점 2자리: {number:.2f}")

    # 문자열 포매팅
    name = "PKNU"
    age = 25
    print(f"      이름: {name}, 나이: {age}세")

    # % 포매팅으로 동일한 결과
    print("      %% 포매팅: 이름: %s, 나이: %d세" % (name, age))

    # format 함수로 동일한 결과
    print("      format 함수: 이름: {}, 나이: {}세".format(name, age))

    # 정렬과 패딩
    print(f"      왼쪽 정렬: '{name:<10}'")
    print(f"      오른쪽 정렬: '{name:>10}'")
    print(f"      가운데 정렬: '{name:^10}'")

    print()
    print("=" * 60)
    print("🎉 환경 테스트 완료! 모든 기능이 정상적으로 작동합니다.")
    print("🚀 이제 알고리즘과 자료구조 실습을 시작할 수 있습니다!")
    print("=" * 60)


if __name__ == "__main__":
    test_python_environment()
