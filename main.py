import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.width = 1000
        self.height = 750

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Rocket Game")

        self.background = pygame.image.load("background.jpg")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        self.font_big = pygame.font.Font("space-nova-font/SpaceFont.otf", 36)
        self.font_small = pygame.font.Font("ascharge-font/smallspacefont.otf", 36)

        self.text1 = ""
        self.text2 = ""
        self.text3 = ""

        self.active_box = None

        self.textbox1 = pygame.Rect(400, 295, 300, 50)
        self.textbox2 = pygame.Rect(400, 360, 300, 50)
        self.textbox3 = pygame.Rect(400, 425, 300, 50)

        self.rocket_dropdown = pygame.Rect(25, 20, 220, 80)
        self.destination_dropdown = pygame.Rect(730, 20, 250, 50)
        self.launched = False
        self.launch_button_rect = pygame.Rect(330, 440, 400, 300)

        self.launch_button = pygame.image.load("Designer.png")
        self.launch_button = pygame.transform.scale(self.launch_button, (400,300))

        self.rocket_options = ["Falcon 9", "SLS", "Starship"]
        self.destination_options = ["ISS", "Moon", "Mars"]

        self.selected_rocket = "Select Rocket"
        self.selected_destination = "Select Destination"

        self.show_rocket_dropdown = False
        self.show_destination_dropdown = False

        self.spacecoin = 0 

        # rocket dict
        self.rocket_prices = {"Falcon 9": 0, "SLS": 250, "Starship": 1000}
        self.unlocked_rockets = {"Falcon 9": True, "SLS": False, "Starship": False}

    def main(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.textbox1.collidepoint(event.pos):
                        self.active_box = 1
                    elif self.textbox2.collidepoint(event.pos):
                        self.active_box = 2
                    elif self.textbox3.collidepoint(event.pos):
                        self.active_box = 3
                    elif self.rocket_dropdown.collidepoint(event.pos):
                        self.show_rocket_dropdown = not self.show_rocket_dropdown
                    elif self.destination_dropdown.collidepoint(event.pos):
                        self.show_destination_dropdown = not self.show_destination_dropdown
                    elif self.launch_button_rect.collidepoint(event.pos):
                        if self.text1 != "" and self.text2 != "" and self.text3 != "" and self.selected_rocket != "Select Rocket" and self.selected_destination != "Select Destination":
                            self.launched = True

                    if self.show_rocket_dropdown:
                        # Falcon 9
                        if pygame.Rect(25, 100, 220, 60).collidepoint(event.pos):
                            if self.unlocked_rockets["Falcon 9"]:
                                self.selected_rocket = "Falcon 9"
                                self.show_rocket_dropdown = False
                        
                        # SLS
                        elif pygame.Rect(25, 160, 220, 60).collidepoint(event.pos):
                            if self.unlocked_rockets["SLS"]:
                                self.selected_rocket = "SLS"
                                self.show_rocket_dropdown = False
                            elif self.spacecoin >= self.rocket_prices["SLS"]:
                                self.spacecoin -= self.rocket_prices["SLS"]
                                self.unlocked_rockets["SLS"] = True
                                self.selected_rocket = "SLS"
                                self.show_rocket_dropdown = False

                        # Starship
                        elif pygame.Rect(25, 220, 220, 60).collidepoint(event.pos):
                            if self.unlocked_rockets["Starship"]:
                                self.selected_rocket = "Starship"
                                self.show_rocket_dropdown = False
                            elif self.spacecoin >= self.rocket_prices["Starship"]:
                                self.spacecoin -= self.rocket_prices["Starship"]
                                self.unlocked_rockets["Starship"] = True
                                self.selected_rocket = "Starship"
                                self.show_rocket_dropdown = False

                    if self.show_destination_dropdown:
                        if pygame.Rect(775, 100, 200, 60).collidepoint(event.pos):
                            self.selected_destination = "ISS"
                            self.show_destination_dropdown = False
                        elif pygame.Rect(775, 160, 200, 60).collidepoint(event.pos):
                            self.selected_destination = "Moon"
                            self.show_destination_dropdown = False
                        elif pygame.Rect(775, 220, 200, 60).collidepoint(event.pos):
                            self.selected_destination = "Mars"
                            self.show_destination_dropdown = False
                
                if event.type == pygame.KEYDOWN:
                    if self.active_box == 1:
                        if event.key == pygame.K_BACKSPACE:
                            self.text1 = self.text1[:-1]
                        else:
                            self.text1 += event.unicode

                    elif self.active_box == 2:
                        if event.key == pygame.K_BACKSPACE:
                            self.text2 = self.text2[:-1]
                        else:
                            self.text2 += event.unicode

                    elif self.active_box == 3:
                        if event.key == pygame.K_BACKSPACE:
                            self.text3 = self.text3[:-1]
                        else:
                            self.text3 += event.unicode

            if not self.launched:
                self.startscreen()
            else:
                print("launched")

            self.screen.blit(self.background, (0,0))
            self.startscreen()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()


    def startscreen(self):
                        
        pygame.draw.rect(self.screen, (255, 255, 255), self.textbox1, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.textbox2, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.textbox3, 2)

        self.screen.blit(self.font_small.render(self.text1, True, (255,255,255)), (410, 305))
        self.screen.blit(self.font_small.render(self.text2, True, (255,255,255)), (410, 370))
        self.screen.blit(self.font_small.render(self.text3, True, (255,255,255)), (410, 435))

        top_text = self.font_big.render("Welcome To Space", True, (255,255, 255))
        text1 = self.font_big.render("Mass:", True, (255, 255, 255))
        text2 = self.font_big.render("Thrust:", True, (255, 255, 255))
        text3 = self.font_big.render("Direction:", True, (255, 255, 255))
        spacecoin_text = self.font_big.render(f"Spacecoin: {self.spacecoin}", True, (175, 175, 175))

        self.screen.blit(top_text, (265, 35))
        self.screen.blit(text1, (248, 305))
        self.screen.blit(text2, (195, 370))
        self.screen.blit(text3, (140, 435))
        
        self.screen.blit(spacecoin_text, (345, 100))
        self.screen.blit(self.launch_button, (330, 440))

        self.rocket_dropdown = pygame.Rect(25, 20, 220, 80)
        self.destination_dropdown = pygame.Rect(775, 20, 200, 80)

        pygame.draw.rect(self.screen, (255, 255, 255), self.rocket_dropdown, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.destination_dropdown, 2)

        if self.selected_rocket != "Select Rocket":
            text_surf = self.font_small.render("Selected", True, (0, 255, 0))
            self.screen.blit(text_surf, (35, 42))
            pygame.draw.lines(self.screen, (0, 255, 0), False, [(162, 55), (167, 62), (177, 48)], 3)
        else:
            self.screen.blit(
                self.font_small.render("Select", True, (255,255,255)),
                (95, 24)
            )
            self.screen.blit(
                self.font_small.render("Rocket", True, (255,255,255)),
                (89, 54)
            )

        if self.selected_destination != "Select Destination":
            text_surf = self.font_small.render("Selected", True, (0, 255, 0))
            self.screen.blit(text_surf, (785, 42))
            pygame.draw.lines(self.screen, (0, 255, 0), False, [(912, 55), (917, 62), (927, 48)], 3)
        else:
            self.screen.blit(
                self.font_small.render("Select", True, (255,255,255)),
                (832, 24)
            )
            self.screen.blit(
                self.font_small.render("Destination", True, (255,255,255)),
                (798, 54)
            )
                
        if self.show_rocket_dropdown:
            for i, option in enumerate(self.rocket_options):
                option_rect = pygame.Rect(25, 100 + i * 60, 220, 60)
                pygame.draw.rect(self.screen, (255,255,255), option_rect, 2)

                if option == self.selected_rocket:
                    color = (0, 255, 0)
                elif self.unlocked_rockets[option]:
                    color = (255, 255, 255)
                elif self.spacecoin >= self.rocket_prices[option]:
                    color = (200, 200, 100)
                else:
                    color = (150, 150, 150)

                if self.unlocked_rockets[option]:
                    text = option
                    if option == self.selected_rocket:
                        text = "> " + option
                    self.screen.blit(self.font_small.render(text, True, color), (35, 115 + i * 60))
                else:

                    name_str = option
                    if option == self.selected_rocket:
                        name_str = "> " + option
                    name_surf = self.font_small.render(name_str, True, color)
                    self.screen.blit(name_surf, (35, 115 + i * 60))

                    if option == "SLS":
                        price_x = 55
                    elif option == "Starship":
                        price_x = 125
                    else:
                        price_x = 140

                    dash_surf = self.font_small.render(" - ", True, color)
                    price_surf = self.font_small.render(str(self.rocket_prices[option]), True, color)
                    
                    y_pos = 115 + i * 60
                    self.screen.blit(dash_surf, (price_x, y_pos))
                    self.screen.blit(price_surf, (price_x + dash_surf.get_width(), y_pos))

        if self.show_destination_dropdown:
            for i, option in enumerate(self.destination_options):
                option_rect = pygame.Rect(775, 100 + i * 60, 200, 60)
                pygame.draw.rect(self.screen, (255, 255, 255), option_rect, 2)

                text = option
                if option == self.selected_destination:
                    text = "> " + option

                color = (0, 255, 0) if option == self.selected_destination else (255, 255, 255)

                self.screen.blit(
                    self.font_small.render(text, True, color),
                    (790, 115 + i * 60)
                )

    def spacecoin(self, km_travelled):
        spacecoin = 0
        while km_travelled > 10000:
            spacecoin += 5
            km_travelled -= 10000
        return spacecoin
        
game = Game()
game.main()
