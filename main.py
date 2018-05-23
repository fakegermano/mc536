from tkinter import StringVar

from ttkthemes.themed_tk import *
from tkinter.ttk import *

MODEL_OPTIONS = [('ESTÁDIO', 'estadio'),
                 ('PARTIDA', 'partida'),
                 ('TIME DE FUTEBOL', 'time'),
                 ('TÉCNICO', 'tecnico'),
                 ('ÁRBITRO', 'arbitro'),
                 ('JOGADOR', 'jogador'),
                 ('TORCEDOR', 'torcedor'),
                 ('COMENTARISTA', 'comentarista'),
                 ('CONSULTAS VARIADAS', 'variadas')]

QUERY_OPTIONS = {'estadio': [],
                 'partida': [],
                 'time': [],
                 'tecnico': [],
                 'arbitro': [],
                 'jogador': [],
                 'torcedor': [],
                 'comentarista': ['Bla'],
                 'variadas': ['Teste 1', 'Teste 2']}  # consultas variadas


class ConsultaFrame(Frame):

    def __init__(self, master=None):
        super(ConsultaFrame, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.left = self.create_left()
        self.right = self.create_right()
        self.left.grid(row=0, column=0, padx=15, pady=15)
        self.right.grid(row=0, column=1, sticky='n', padx=30, pady=30)

    def create_left(self):
        left = Frame(self)
        self.model = StringVar()
        self.model.set('variadas')
        self.model.trace("w", self.update_combo)
        Label(left, text="1º Selecione uma opção").grid(row=0, column=0)
        for i, opt in enumerate(MODEL_OPTIONS):
            Radiobutton(left, text=opt[0], value=opt[1], variable=self.model).grid(row=i+1, column=0, sticky='w')
        return left

    def create_right(self):
        right = Frame(self)
        s = Style()
        s.configure('Sair.TButton', foreground="#f00")
        Label(right, text="2º por favor escolha a consulta").pack()
        self.query = StringVar()
        self.query.set('-------')
        self.box = Combobox(right, exportselection=True, justify='left', height=5,
                            state='readonly', values=QUERY_OPTIONS[self.model.get()], textvariable=self.query)
        self.box.pack(fill='x')
        Button(right, text='Pesquisar', command=self.search).pack()
        Button(right, text='Sair', command=root.destroy, style='Sair.TButton').pack()
        return right

    def update_combo(self, *args):
        self.box.configure(values=QUERY_OPTIONS[self.model.get()])
        self.query.set('-------')
        self.box.pack()

    def search(self):
        if self.query.get() == '-------':
            return
        print(self.model.get())
        print(self.query.get())


class NovaFrame(Frame):
    def __init__(self, master=None):
        super(NovaFrame, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Aqui vão as inserções").pack(side="top")
        Button(self, text='Sair', command=root.destroy, style='Sair.TButton').pack(side="bottom")

class Tabs(Notebook):

    def __init__(self, master=None):
        super().__init__(master)
        self.add_tabs()
        self.pack()

    def add_tabs(self):
        query = ConsultaFrame(self)
        lookup = NovaFrame(self)
        self.add(query, text="CONSULTA(S)")
        self.add(lookup, text="NOVA(S) ENTRADA(S)")


if __name__ == "__main__":
    root = ThemedTk()
    root.title("Consultas e Inserções")
    root.maxsize(800, 600)
    root.set_theme('arc')

    note = Tabs(root)
    root.mainloop()
    exit()
else:
    exit()
