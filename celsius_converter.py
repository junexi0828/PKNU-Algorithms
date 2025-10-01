#!/usr/bin/env python3
"""
Celsius Temperature Converter
섭씨 온도 변환기 - 섭씨와 화씨 간 온도 변환을 수행합니다.
"""


def celsius_to_fahrenheit(celsius):
    """섭씨를 화씨로 변환합니다."""
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """화씨를 섭씨로 변환합니다."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def main():
    """메인 함수 - 온도 변환 프로그램을 실행합니다."""

    print("=" * 50)
    print("🌡️  섭씨 온도 변환기 (Celsius Converter)")
    print("=" * 50)

    while True:
        print("\n변환 옵션을 선택하세요:")
        print("1. 섭씨 → 화씨 (Celsius to Fahrenheit)")
        print("2. 화씨 → 섭씨 (Fahrenheit to Celsius)")
        print("3. 종료 (Exit)")

        choice = input("\n선택 (1-3): ").strip()

        if choice == "1":
            try:
                celsius = float(input("섭씨 온도를 입력하세요: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"📊 결과: {celsius}°C = {fahrenheit:.2f}°F")
            except ValueError:
                print("❌ 올바른 숫자를 입력해주세요.")

        elif choice == "2":
            try:
                fahrenheit = float(input("화씨 온도를 입력하세요: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"📊 결과: {fahrenheit}°F = {celsius:.2f}°C")
            except ValueError:
                print("❌ 올바른 숫자를 입력해주세요.")

        elif choice == "3":
            print("🎉 온도 변환기를 종료합니다. 감사합니다!")
            break

        else:
            print("❌ 1, 2, 3 중에서 선택해주세요.")


if __name__ == "__main__":
    main()
