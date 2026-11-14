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

        self.textbox1 = pygame.Rect(370, 325, 300, 50)
        self.textbox2 = pygame.Rect(370, 390, 300, 50)
        self.textbox3 = pygame.Rect(370, 455, 300, 50)

        self.rocket_dropdown = pygame.Rect(25, 20, 200, 80)
        self.destination_dropdown = pygame.Rect(730, 20, 250, 50)

        self.rocket_options = ["Falcon 9", "SLS", "Starship"]
        self.destination_options = ["ISS", "Moon", "Mars"]

        self.selected_rocket = "Select Rocket"
        self.selected_destination = "Select Destination"

        self.show_rocket_dropdown = False
        self.show_destination_dropdown = False

        self.tick_font = pygame.font.Font(None, 36)


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

                    if self.show_rocket_dropdown:
                        if pygame.Rect(25, 100, 200, 60).collidepoint(event.pos):
                            self.selected_rocket = "Falcon 9"
                        elif pygame.Rect(25, 160, 200, 60).collidepoint(event.pos):
                            self.selected_rocket = "SLS"
                        elif pygame.Rect(25, 220, 200, 60).collidepoint(event.pos):
                            self.selected_rocket = "Starship"

                    if self.show_destination_dropdown:
                        if pygame.Rect(775, 100, 200, 60).collidepoint(event.pos):
                            self.selected_destination = "ISS"
                        elif pygame.Rect(775, 160, 200, 60).collidepoint(event.pos):
                            self.selected_destination = "Moon"
                        elif pygame.Rect(775, 220, 200, 60).collidepoint(event.pos):
                            self.selected_destination = "Mars"
                
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

            self.screen.blit(self.background, (0,0))
            self.startscreen()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()


    def startscreen(self):
                        
        pygame.draw.rect(self.screen, (255, 255, 255), self.textbox1, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.textbox2, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.textbox3, 2)

        self.screen.blit(self.font_small.render(self.text1, True, (255,255,255)), (380, 335))
        self.screen.blit(self.font_small.render(self.text2, True, (255,255,255)), (380, 400))
        self.screen.blit(self.font_small.render(self.text3, True, (255,255,255)), (380, 465))

        top_text = self.font_big.render("Welcome To Space", True, (255,255, 255))
        text1 = self.font_big.render("Mass:", True, (255, 255, 255))
        text2 = self.font_big.render("Thrust:", True, (255, 255, 255))
        text3 = self.font_big.render("Direction:", True, (255, 255, 255))

        self.screen.blit(top_text, (265,35))
        self.screen.blit(text1, (218, 335))
        self.screen.blit(text2, (165, 400))
        self.screen.blit(text3, (110, 465))

        self.launch_button = pygame.image.load("Designer.png")
        self.launch_button = pygame.transform.scale(self.launch_button, (400,300))
        self.screen.blit(self.launch_button, (320,470))

########################################################################################################################################

        self.rocket_dropdown = pygame.Rect(25, 20, 200, 80)
        self.destination_dropdown = pygame.Rect(775, 20, 200, 80)

        pygame.draw.rect(self.screen, (255, 255, 255), self.rocket_dropdown, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.destination_dropdown, 2)


        self.screen.blit(
            self.font_small.render("Select", True, (255,255,255)),
            (85, 24)
        )

        self.screen.blit(
            self.font_small.render("Rocket", True, (255,255,255)),
            (79, 54)
        )

        if self.selected_rocket != "Select Rocket":
            pygame.draw.rect(self.screen, (255,255,255), (40, 52, 12, 12))

 
        self.screen.blit(
            self.font_small.render("Select", True, (255,255,255)),
            (832, 24)
        )

        self.screen.blit(
            self.font_small.render("Destination", True, (255,255,255)),
            (798, 54)
        )

#############################################################################################################################################
       
        if self.selected_destination != "Select Destination":
            pygame.draw.rect(self.screen, (255,255,255), (780, 52, 12, 12))
                
        if self.show_rocket_dropdown:
            for i, option in enumerate(self.rocket_options):
                option_rect = pygame.Rect(25, 100 + i * 60, 200, 60)
                pygame.draw.rect(self.screen, (255,255,255), option_rect, 2)

                text = option
                if option == self.selected_rocket:
                    text = "> " + option

                self.screen.blit(
                    self.font_small.render(text, True, (255,255,255)),
                    (40, 115 + i * 60)
                )

        if self.show_destination_dropdown:
            for i, option in enumerate(self.destination_options):
                option_rect = pygame.Rect(775, 100 + i * 60, 200, 60)
                pygame.draw.rect(self.screen, (255,255,255), option_rect, 2)

                text = option
                if option == self.selected_destination:
                    text = "> " + option

                self.screen.blit(
                    self.font_small.render(text, True, (255,255,255)),
                    (790, 115 + i * 60)
                )
                
game = Game()
game.main()
