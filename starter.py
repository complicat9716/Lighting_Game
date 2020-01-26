import pygame

pygame.init()
print("game code")

hero_rect = pygame.Rect(100, 500, 120, 125)

print("origin (%d, %d)" % (hero_rect.x, hero_rect.y))
print("size (%d, %d)" % (hero_rect.width, hero_rect.height))
print("size (%d, %d)" % hero_rect.size)

pygame.quit()