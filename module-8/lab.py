###### 8.9 Car value (classes)
# Complete the Car class by creating an attribute purchase_price (type int)
# and the method print_info() that outputs the car's information.
# class Car:
#     def __init__(self):
#         self.model_year = 0
#         self.purchase_price = 0

#         self.current_value = 0

#     def calc_current_value(self, current_year):
#         depreciation_rate = 0.15
#         # Car depreciation formula
#         car_age = current_year - self.model_year
#         self.current_value = round(
#             self.purchase_price * (1 - depreciation_rate) ** car_age)

#     def print_info(self):
#         print(f'Car\'s information:'
#               f'\n   Model year: {self.model_year}'
#               f'\n   Purchase price: {self.purchase_price}'
#               f'\n   Current value: {self.current_value}')


# if __name__ == "__main__":
#     year = int(input())
#     price = int(input())
#     current_year = int(input())

#     my_car = Car()
#     my_car.model_year = year
#     my_car.purchase_price = price
#     my_car.calc_current_value(current_year)
#     my_car.print_info()

###### 8.10 LAB: Winning team (classes)
# Complete the Team class implementation. For the instance method get_win_percentage(), the formula is:
# team_wins / (team_wins + team_losses)
#Note: Use floating-point division.
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == "__main__":
    
    team = Team()
   
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())
    
    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses
    
    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name,'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')