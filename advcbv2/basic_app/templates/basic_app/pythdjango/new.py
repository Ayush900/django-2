class english_cups():
    sixth = 'manutd'

    def __init__(self,winners,runner_up):
        self.winners = winners
        self.runner_up = runner_up
bpl = english_cups(winners='liverpool',runner_up='mancity')
FA_Cup = english_cups(winners='arsenal',runner_up='chelsea')
print("The winner of the bpl is {} and the runner up is {} and sixth is {}.".format(bpl.winners,bpl.runner_up,bpl.sixth))
print("The winner of the FA Cup is {} and the runner up is {} and sixth is {}.".format(FA_Cup.winners,FA_Cup.runner_up,bpl.sixth))
