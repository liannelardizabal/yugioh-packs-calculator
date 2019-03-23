class YugiohPacksCalculator:
    def __init__(self, deck_size, special_cards, total_special):
        self.deck_size = deck_size
        self.special_cards = special_cards
        self.total_special = total_special

    def calculate_packs(self):
        deck_size = self.deck_size
        special_cards = self.special_cards
        total_special = self.total_special

        draws = special_cards * (deck_size + total_special) / (total_special + 1)

        return draws

    def calculate_gems(self):
        gems = self.calculate_packs() * 50
        return gems

ypc = YugiohPacksCalculator(200, 3, 6)

print(ypc.calculate_packs())
print(ypc.calculate_gems())
