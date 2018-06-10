from tkinter import StringVar, Toplevel, IntVar
from tkinter.messagebox import showinfo

from ttkthemes.themed_tk import *
from tkinter.ttk import *

MODEL_OPTIONS = {'estadio': 'ESTADIO',
                 'partida': 'PARTIDA',
                 'time': 'TIME DE FUTEBOL',
                 'tecnico': 'TECNICO',
                 'arbitro': 'ARBITRO',
                 'jogador': 'JOGADOR',
                 'torcedor': 'TORCEDOR',
                 'comentarista': 'COMENTARISTA',
                 'variadas': 'CONSULTAS VARIADAS'}

ESTADIO_QUERY_TEXTS = ['Partidas realizadas neste estádio', 'Estádios participantes na Copa']
ESTADIO_QUERY_CODES = ['E1', 'E2']

PARTIDA_QUERY_TEXTS = ['Estádio onde a partida foi realizada', 'Árbitros apitando a partida',
                       'Comentaristas narrando a partida', 'Torcedors presentes na partida',
                       'Times jogando a partida', 'Partidas realizadas na copa']
PARTIDA_QUERY_CODES = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']

TIME_QUERY_TEXTS = ['Times contra quem o time jogou', 'Técnico do time',
                    'Jogadores do time', 'Torcedores do time', 'Times participando da Copa']
TIME_QUERY_CODES = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']

TECNICO_QUERY_TEXTS = ['Time que participa', 'Jogadores que treina']
TECNICO_QUERY_CODES = ['C1', 'C2']

ARBITRO_QUERY_TEXTS = ['Partidas que apitou', 'Árbitros na Copa']
ARBITRO_QUERY_CODES = ['A1', 'A2']

JOGADOR_QUERY_TEXTS = ['Time que participa', 'Técnico que o treina', 'Jogadores na Copa']
JOGADOR_QUERY_CODES = ['J1', 'J2', 'J3']

TORCEDOR_QUERY_TEXTS = ['Time que torce', 'Partidas que assistiu', 'Torcedores na Copa']
TORCEDOR_QUERY_CODES = ['F1', 'F2', 'F3']

COMENTARISTA_QUERY_TEXTS = ['Partidas que narrou', 'Comentaristas na Copa']
COMENTARISTA_QUERY_CODES = ['N1', 'N2']

VARIADAS_QUERY_TEXTS = ['Comentaristas que narraram em uma partidas em que o Brasil jogou',
                        'Torcedores que não foram para nenhum jogo do Brasil',
                        'Jogadores de defesa que não levaram nenhum cartão',
                        'Partidas com mais de 2000 torcedores',
                        'Estádio com menos que 2 partidas',
                        'Em quais estádios árbitros brasileiros vão apitar uma partida',
                        'Jogadores que levaram um ou mais cartões vermelhos',
                        'Jogadores que fizeram 3 ou mais gols',
                        'Estádio com capacidade inferior a 30000 pessoas',
                        'Times cujos jogadores somam menos de 20 cartões amarelos',
                        'Árbitro que foi mais de 3 vezes bandeirinha',
                        'Árbitro que deu mais que 8 cartões vermelhos ou amarelos',
                        'Comentaristas que narraram mais de 30 gols',
                        'Torcedor que assistiu partidas que o camisa 10 do Brasil jogou',
                        'Comentaristas que narraram partidas em que um dos times jogava com formação 4-4-3']
VARIADAS_QUERY_CODES = ['#1', '#2', '#3', '#4', '#5',
                        '#6', '#7', '#8', '#9', '#10',
                        '#11', '#12', '#13', '#14', '#15']

QUERY_OPTIONS = {'estadio': ESTADIO_QUERY_TEXTS,
                 'partida': PARTIDA_QUERY_TEXTS,
                 'time': TIME_QUERY_TEXTS,
                 'tecnico': TECNICO_QUERY_TEXTS,
                 'arbitro': ARBITRO_QUERY_TEXTS,
                 'jogador': JOGADOR_QUERY_TEXTS,
                 'torcedor': TORCEDOR_QUERY_TEXTS,
                 'comentarista': COMENTARISTA_QUERY_TEXTS,
                 'variadas': VARIADAS_QUERY_TEXTS}  # consultas variadas

QUERY_OPTIONS_CODES = {'estadio': ESTADIO_QUERY_CODES,
                       'partida': PARTIDA_QUERY_CODES,
                       'time': TIME_QUERY_CODES,
                       'tecnico': TECNICO_QUERY_CODES,
                       'arbitro': ARBITRO_QUERY_CODES,
                       'jogador': JOGADOR_QUERY_CODES,
                       'torcedor': TORCEDOR_QUERY_CODES,
                       'comentarista': COMENTARISTA_QUERY_CODES,
                       'variadas': VARIADAS_QUERY_CODES}


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
        for i, opt in enumerate([(k, v) for k, v in MODEL_OPTIONS.items()]):
            Radiobutton(left, text=opt[1], value=opt[0], variable=self.model).grid(row=i+1, column=0, sticky='w')
        return left

    def create_right(self):
        right = Frame(self)
        s = Style()
        s.configure('Sair.TButton', foreground="#f00")
        Label(right, text="2º por favor escolha a consulta").pack()
        self.query = StringVar()
        self.query.set('-------')
        self.box = Combobox(right, exportselection=False, justify='left', height=8,
                            state='readonly', values=QUERY_OPTIONS[self.model.get()],
                            textvariable=self.query)
        self.box.pack(fill='x', pady=20)
        Button(right, text='Avançar', command=self.get_info).pack()
        Button(right, text='Sair', command=root.destroy, style='Sair.TButton').pack(pady=20)
        return right

    def update_combo(self, *args):
        self.box.configure(values=QUERY_OPTIONS[self.model.get()])
        self.query.set('-------')
        self.box.pack()

    def get_info(self):
        if self.query.get() == '-------':
            return

        info = Toplevel()
        info.title("Mais Informações")
        frame = Frame(info)
        query_code = QUERY_OPTIONS_CODES[self.model.get()][self.box.current()]
        self.info = StringVar()
        Label(frame, text="Código da Query: %s\tModelo Relacionado: %s"
                          % (query_code, MODEL_OPTIONS[self.model.get()])).pack(pady=15, padx=5)
        Label(frame, text="Informe as informações extra necessárias").pack(pady=5, padx=5)
        Entry(frame, textvariable=self.info).pack(fill='x', padx=30)
        Button(frame, text="Pesquisar", command=lambda: self.do_query(info, query_code)).pack(pady=15)

        frame.pack()

    def do_query(self, popup, qcode):

        showinfo("Resultados", "Pesquisando query %s com atributo %s" % (qcode, self.info.get()))
        popup.destroy()


class NovaFrame(Frame):
    def __init__(self, master=None):
        super(NovaFrame, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Selecione o que você quer inserir").pack(side="top", pady=15)
        self.inputvalue = StringVar()
        options = list(MODEL_OPTIONS.values())[:-2]
        options.extend(['ASSISTE', 'NARRA', 'APITA', 'JOGA CONTRA'])
        self.input = Combobox(self, exportselection=True,
                              justify='left', height=6,
                              state='readonly', values=options,
                              textvariable=self.inputvalue)
        self.input.pack(fill='x', padx=15)
        Button(self, text='Inserir', command=self.insert).pack()
        Button(self, text='Atualizar', command=self.update).pack()
        Button(self, text='Sair', command=root.destroy, style='Sair.TButton').pack(side="bottom", pady=15)

    def insert_torcedor(self, frame):
        self.doc_id = IntVar()
        self.doc_type = StringVar()
        self.country = StringVar()
        self.country_fan = StringVar()  # must be referencing a country in db
        Label(frame, text="Inserindo um torcedor").pack(padx=15, pady=15)
        innerframe = Frame(frame)
        Label(innerframe, text="Numero do Documento").grid(row=0, column=0)
        Entry(innerframe, textvariable=self.doc_id).grid(row=0, column=1)
        Label(innerframe, text="Tipo de Documento").grid(row=1, column=0)
        Entry(innerframe, textvariable=self.doc_type).grid(row=1, column=1)
        Label(innerframe, text="País de origem").grid(row=2, column=0)
        Entry(innerframe, textvariable=self.country).grid(row=2, column=1)
        Label(innerframe, text="País que torce").grid(row=3, column=0)
        Combobox(innerframe, exportselection=True, justify='center', height=6, state='readonly',
                 values=self.get_countries(), textvariable=self.country_fan).grid(row=3, column=1)
        innerframe.pack()

    def insert_comentarista(self, frame):
        self.doc_id = IntVar()
        self.doc_type = StringVar()
        self.country = StringVar()
        self.language = StringVar()  # must be referencing a country in db
        Label(frame, text="Inserindo um torcedor").pack(padx=15, pady=15)
        innerframe = Frame(frame)
        Label(innerframe, text="Numero do Documento").grid(row=0, column=0)
        Entry(innerframe, textvariable=self.doc_id).grid(row=0, column=1)
        Label(innerframe, text="Tipo de Documento").grid(row=1, column=0)
        Entry(innerframe, textvariable=self.doc_type).grid(row=1, column=1)
        Label(innerframe, text="País de origem").grid(row=2, column=0)
        Entry(innerframe, textvariable=self.country).grid(row=2, column=1)
        Label(innerframe, text="Língua").grid(row=3, column=0)
        Entry(innerframe, textvariable=self.language).grid(row=3, column=1)
        innerframe.pack()

    def insert_arbitro(self, frame):
        self.doc_id = IntVar()
        self.doc_type = StringVar()
        self.country = StringVar()
        self.role = StringVar()  # must be referencing a country in db
        Label(frame, text="Inserindo um torcedor").pack(padx=15, pady=15)
        innerframe = Frame(frame)
        Label(innerframe, text="Numero do Documento").grid(row=0, column=0)
        Entry(innerframe, textvariable=self.doc_id).grid(row=0, column=1)
        Label(innerframe, text="Tipo de Documento").grid(row=1, column=0)
        Entry(innerframe, textvariable=self.doc_type).grid(row=1, column=1)
        Label(innerframe, text="País de origem").grid(row=2, column=0)
        Entry(innerframe, textvariable=self.country).grid(row=2, column=1)
        Label(innerframe, text="Função").grid(row=3, column=0)
        Entry(innerframe, textvariable=self.role).grid(row=3, column=1)
        innerframe.pack()

    def insert(self):
        insertwin = Toplevel()
        insertwin.wm_title('Inserir')
        insertframe = Frame(insertwin)
        error = False
        if self.inputvalue.get() == MODEL_OPTIONS['torcedor']:
            self.insert_torcedor(insertframe)
        elif self.inputvalue.get() == MODEL_OPTIONS['comentarista']:
            self.insert_comentarista(insertframe)
        elif self.inputvalue.get() == MODEL_OPTIONS['arbitro']:
            self.insert_arbitro(insertframe)
        elif self.inputvalue.get() == MODEL_OPTIONS['time']:
            self.insertinfo = StringVar()
            Label(insertframe, text="Inserindo um time").pack(padx=15, pady=15)
            Entry(insertframe, textvariable=self.insertinfo).pack()
        elif self.inputvalue.get() == MODEL_OPTIONS['estadio']:
            self.insertinfo = StringVar()
            Label(insertframe, text="Inserindo um estádio").pack(padx=15, pady=15)
            Entry(insertframe, textvariable=self.insertinfo).pack()
        elif self.inputvalue.get() == MODEL_OPTIONS['tecnico']:
            self.insertinfo = StringVar()
            Label(insertframe, text="Inserindo um técnico").pack(padx=15, pady=15)
            Entry(insertframe, textvariable=self.insertinfo).pack()
        elif self.inputvalue.get() == MODEL_OPTIONS['jogador']:
            self.insertinfo = StringVar()
            Label(insertframe, text="Inserindo um jogador").pack(padx=15, pady=15)
            Entry(insertframe, textvariable=self.insertinfo).pack()
        elif self.inputvalue.get() == MODEL_OPTIONS['partida']:
            self.insertinfo = StringVar()
            Label(insertframe, text="Inserindo uma partida").pack(padx=15, pady=15)
            Entry(insertframe, textvariable=self.insertinfo).pack()
        elif self.inputvalue.get() == 'ASSISTE':
            self.insertinfo = StringVar()
            Label(insertframe, text="Relacionando um torcedor com uma partida").pack(padx=15, pady=15)
            Entry(insertframe, textvariable=self.insertinfo).pack()
        elif self.inputvalue.get() == 'NARRA':
            self.insertinfo = StringVar()
            Label(insertframe, text="Relacionando um narrador com uma partida").pack(padx=15, pady=15)
            Entry(insertframe, textvariable=self.insertinfo).pack()
        elif self.inputvalue.get() == 'APITA':
            self.insertinfo = StringVar()
            Label(insertframe, text="Relacionando um árbitro com uma partida").pack(padx=15, pady=15)
            Entry(insertframe, textvariable=self.insertinfo).pack()
        elif self.inputvalue.get() == 'JOGA CONTRA':
            self.insertinfo = StringVar()
            Label(insertframe, text="Relacionando times com times").pack(padx=15, pady=15)
            Entry(insertframe, textvariable=self.insertinfo).pack()
        else:
            self.insertinfo = StringVar()
            Label(insertframe, text="Selecione um modelo válido").pack(padx=15, pady=15)
            error = True
        if error is True:
            Button(insertframe, text="Voltar", command=insertwin.destroy).pack(pady=15)
        else:
            Button(insertframe, text="Salvar", command=insertwin.destroy).pack(pady=15)
        insertframe.pack()

    def get_countries(self):
        return ['Brasil', 'Alemanha', 'Espanha']  # TODO: trocar por uma query no BD

    def update(self):
        updatewin = Toplevel()
        updatewin.wm_title('Atualizar')
        updateframe = Frame(updatewin)
        self.updateinfo = StringVar()
        Label(updateframe, text="Coloque aqui informações extas").pack(padx=15, pady=15)
        Entry(updateframe, textvariable=self.updateinfo).pack()
        Button(updateframe, text="Salvar", command=updatewin.destroy).pack(pady=15)
        updateframe.pack()


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
    root.set_theme('arc')
    note = Tabs(root)
    root.mainloop()
    exit()
else:
    exit()
