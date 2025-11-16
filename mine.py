from ursina import *

class Voxel(Button):
    def _init_(self, position=(0,0,0)):
        super()._init_(
            parent=scene,
            model='cube',
            texture='white_cube',
            color=color.brown,
            position=position,
            highlight_color=color.lime
        )

    def on_click(self):
        destroy(self)  # ЛКМ удаляет блок

    def on_right_click(self):
        new_voxel = Voxel(position=self.position + mouse.normal)  # ПКМ ставит блок


class Minecraft(Ursina):
    def _init_(self):
        super()._init_()
        self.init_world()
        self.init_player()

    def init_world(self):
        # Генерируем землю 10x10
        for x in range(10):
            for z in range(10):
                Voxel(position=(x, 0, z))

    def init_player(self):
        self.player = FirstPersonController()

    def update(self):
        if held_keys['escape']:
            application.quit()

if _name_ == '_main_':
    game = Minecraft()
    game.run()