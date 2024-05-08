from abc import ABC, abstractmethod

# Target 인터페이스
class Missile(ABC):
    @abstractmethod
    def launch(self):
        pass

# Adaptee 클래스
class ForeignMissile:
    def fire(self):
        print("Foreign Missile has been fired!")

# Adapter 클래스
class ForeignMissileAdapter(Missile):
    def __init__(self, foreign_missile):
        self.foreign_missile = foreign_missile

    def launch(self):
        # Adapter가 Target 인터페이스를 구현하도록 Adaptee의 메서드를 호출.
        self.foreign_missile.fire()

# Singleton 패턴을 이용한 발사 제어 시스템
class LaunchControlSystem:
    _instance = None

    def __new__(cls):
        # 하나의 인스턴스만을 생성하기 위해 싱글톤 패턴을 사용.
        if cls._instance is None:
            cls._instance = super(LaunchControlSystem, cls).__new__(cls)
        return cls._instance

    def launch_missile(self, missile):
        # 발사 제어 시스템에서 미사일을 발사하는 method.
        missile.launch()

# Factory 패턴을 이용한 미사일 생성
class MissileFactory:
    @staticmethod
    def create_missile(missile_type):
        # 입력된 미사일 타입에 따라 해당하는 미사일 객체를 생성하여 반환.
        if missile_type == "ICBM":
            return ICBMMissile()
        elif missile_type == "Cruise":
            return CruiseMissile()
        elif missile_type == "SLBM":
            return SLBMMissile()
        elif missile_type == "Ballistic":
            return BallisticMissile()
        elif missile_type == "Foreign":
            return ForeignMissileAdapter(ForeignMissile())
        else:
            raise ValueError("Unknown missile type")

class ICBMMissile(Missile):
    def launch(self):
        # ICBM 미사일을 발사하는 method.
        print("ICBM Missile has been launched!")

class CruiseMissile(Missile):
    def launch(self):
        # Cruise 미사일을 발사하는 method.
        print("Cruise Missile has been launched!")

class SLBMMissile(Missile):
    def launch(self):
        # SLBM 미사일을 발사하는 method.
        print("SLBM Missile has been launched!")

class BallisticMissile(Missile):
    def launch(self):
        # Ballistic 미사일을 발사하는 method.
        print("Ballistic Missile has been launched!")

def get_user_confirmation():
    # 사용자로부터 발사 승인 여부를 확인하는 함수.
    response = input("발사 승인하시겠습니까? (y/n): ").lower()
    return response == 'y'

# 사용 예시
control_system = LaunchControlSystem()

while True:
    missile_type = input("발사할 미사일 종류를 입력하거나(ICBM, Cruise, SLBM, Ballistic, Foreign) 종료하려면 'exit'를 입력하세요: ")
    if missile_type == 'exit':
        print("발사 절차를 종료합니다.")
        break

    if missile_type in ["ICBM", "Cruise", "SLBM", "Ballistic", "Foreign"]:
        if get_user_confirmation():
            # 미사일을 생성하고 발사.
            missile = MissileFactory.create_missile(missile_type)
            control_system.launch_missile(missile)
            print("미사일이 발사되었습니다. 발사 절차를 종료합니다.")
            break
        else:
            print("미사일 발사가 취소되었습니다. 발사 절차를 종료합니다.")
            break
    else:
        print("다시 입력해주세요.")
