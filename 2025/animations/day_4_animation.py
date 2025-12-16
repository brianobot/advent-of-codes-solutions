import time
import pygame
from pathlib import Path

from ..day_4 import read_input_data, calculate_total_accessible_paper_roll


BASE_DIR = Path(__file__).parent

pygame.init()

# FONT SETUP
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 20)


WIDTH, HEIGHT = (pygame.display.Info().current_w, pygame.display.Info().current_h) # Pixels
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Advent of Code Day 4 Animation @ By Brian Obot")


def draw(grid: list[list[str]], total: int, status: str):
    WIN.fill("black")
    
    text = FONT.render(f"Total: {total:}", 1, "blue")
    WIN.blit(text, (5, 0))
    
    text = FONT.render(f"Status: {status:}", 1, "green")
    WIN.blit(text, (5, 25))
    
    texts = []
    for x_index, row in enumerate(grid):
        for y_index, col in enumerate(row):
            coord_text = FONT.render(f"{col}", 1, "white")
            texts.append(
                (
                    coord_text, 
                    (
                        (y_index * 10) + 50, 
                        (x_index * 10) + 50
                    )
                )
            )
            
    WIN.blits(texts)
    pygame.display.update()


def main(grid: list[list[str]]):
    
    running = True
    clock = pygame.time.Clock()
    main_total = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        total, grid = calculate_total_accessible_paper_roll(grid)
        main_total += total
        status = "Running" if total else "Completed"
        draw(grid, main_total, status)
    
        clock.tick(1)
                
    pygame.quit()


if __name__ == "__main__":
    grid = read_input_data()
    main(grid)