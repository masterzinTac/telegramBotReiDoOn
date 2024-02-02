import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold
from aiogram import F
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


TOKEN = '6870617231:AAElFRc9CsPwWv-0reJaYdShfUs5sAwY1_0'
dp = Dispatcher()

class MyCallback(CallbackData, prefix="my"):
    data_code: str
    
    
    
class Form(StatesGroup):
    comprovante = State()
    compchatid = State()
    complinkacesso = State()
    
    
    
def keyboard_presente():
    builder = InlineKeyboardBuilder()
    builder.button(
    text="PRESENTINHO 🎁",
    callback_data=MyCallback(data_code="button_presente")
    )
    return builder.as_markup()



@dp.message(CommandStart())
async def menu_start(message: Message):
    await message.answer("""
        Olá, Seja bem vindo ao 🔞 Rei do Only 🔞

Somos um dos maiores grupos de Onlyfans do Brasil 🇧🇷

Ja somos mais de 50 mil mídias de conteúdos exclusivos das mulheres mais procuradas da internet 😎""")
    await menu_presente(message)
    chatid = message.chat.id
    
    

async def menu_presente(message: Message):
    await message.answer("""
        Bom, então to te devendo um presente né? 🤭 
Aqui, promessa é divida, resgate seus vídeos 😈👇""", reply_markup=keyboard_presente())




@dp.callback_query(MyCallback.filter(F.data_code == "button_presente"))
async def button_presente_logic(query: CallbackQuery, callback_data: MyCallback):
    #await query.message.answer(f"Mensagem Data {callback_data}") DEBUG DEBUG
    await entrega_presente(query.message)
    

async def entrega_presente(message: Message):
    await message.answer("--- PRESENTE PLACEHOLDER ---")
    await menu_lista(message)




def keyboard_lista():
    builder = InlineKeyboardBuilder()
    builder.button(
    text="SIM 😎",
    callback_data=MyCallback(data_code="button_lista_confirm")
    )
    return builder.as_markup()


async def menu_lista(message: Message):
    await message.answer("🔥Eae gostou? Tem muito mais de onde veio esses 🤫 voce teria 2 minutinhos para dar uma olhadinha na nossa lista de garotas?", reply_markup=keyboard_lista())


@dp.callback_query(MyCallback.filter(F.data_code == "button_lista_confirm"))
async def button_lista_confirm_logic(query: CallbackQuery, callback_data: MyCallback):
    #await query.message.answer(f"Mensagem Data {callback_data}") #DEBUG DEBUG
    await entrega_lista(query.message)



async def entrega_lista(message: Message):
    await message.answer(f"""Agora {hbold(message.chat.first_name)}🗿🍷 imagina você ter acesso a uma 
lista com mais de {hbold("2 MIL OnlyFans em um so lugar 😎")}""")
    await message.answer("---FOTO LISTA PLACEHOLDER---")
    await message.answer("""Veja algumas das garotas que você
vai receber ao entrar no nosso grupo VIP 😎🔞
CibellyFerreira
Mc Pipokinha
TatiZaqui""")
    await message.answer("--- FOTO PLACEHOLDER ---")
    await menu_compra(message)



async def menu_compra(message: Message):
    await message.answer(f"""Gostou? 🙃

Agora imagina você abrir o site do Onlyfans e ter acesso a {hbold("PRATICAMENTE TODAS AS GAROTAS DO SITE")} 😎
bom não precisa imaginar mais. Nosso grupo é exatemente isso🥱

E sabe qual o melhor? Estamos em promoção, você vai ter acesso a tudo isso e muito mais.
VEJA ESSE SUPER DESCONTO QUE CONSEGUI PRA VC 🤭👇

✅ DESCONTO LIBERADO ✅

🚨 {hbold("ACESSO VITALÍCIO POR APENAS R$ 14,90")} 🚨

 VOCÊ SÓ PAGA UMA VEZ 😎""")
    
    await menu_compra_confirmacao(message)


def keyboard_compra():
    builder = InlineKeyboardBuilder()
    builder.button(
    text="Entrar para o VIP 🔞",
    callback_data=MyCallback(data_code="button_compra")
    )
    return builder.as_markup()


async def menu_compra_confirmacao(message: Message):
    await message.answer("Clique no botão abaixo para fazer sua inscrição 👇",reply_markup=keyboard_compra())

@dp.callback_query(MyCallback.filter(F.data_code == "button_compra"))
async def button_compra_logic(query: CallbackQuery, callback_data: MyCallback):
    #await query.message.answer(f"Mensagem Data {callback_data}") #DEBUG DEBUG
    await menu_compra_pix(query.message)
    
def keyboard_next_step():
    builder = InlineKeyboardBuilder()
    builder.button(
    text="Próxima Etapa 👉",
    callback_data=MyCallback(data_code="button_next_step")
    )
    builder.button(
    text="Falar Com Suporte ⚠️",
    callback_data=MyCallback(data_code="button_suporte")
    )
    return builder.as_markup()

async def menu_compra_pix(message: Message):
    await message.answer(f"""Para Acessar o Grupo VIP Faça o {hbold("Pagamento de 14,90 R$")} Para Este PIX (Chave Aleatória)
                   
        {hbold("Chave Pix: CHAVE PIX PLACEHOLDER")}
                   
Logo após o pagamento clique no botão abaixo para a próxima etapa.
Ou clique em falar com o suporte para resolver os problemas com sua compra
                   """, reply_markup=keyboard_next_step())
    

@dp.callback_query(MyCallback.filter(F.data_code == "button_next_step"))
async def button_next_step_logic(query: CallbackQuery, callback_data: MyCallback, state: FSMContext) -> None:
    #await query.message.answer(f"Mensagem Data {callback_data}") #DEBUG DEBUG
    await state.set_state(Form.comprovante)
    await query.message.answer(f"""Envie {hbold("APENAS")} a foto do comprovante de compra e aguarde.""")
    
@dp.callback_query(MyCallback.filter(F.data_code == "button_suporte"))
async def button_suporte_logic(query: CallbackQuery, callback_data: MyCallback):
    #await query.message.answer(f"Mensagem Data {callback_data}") #DEBUG DEBUG
    await query.message.answer(f"""Envie sua mensagem para um de nossos moderadores sua duvida será resolvida rapidamente 👇
            
    {("Nosso Moderador: @tackzin")}""")
        


@dp.message(Form.comprovante, F.photo)
async def processar_comprovante(message: Message, state: FSMContext, bot: Bot) -> None:
    await state.update_data(comprovante=message.photo)
    await message.answer(f"""Muito obrigado, você agora só precisa aguardar um dos nossos moderadores analisar sua compra. 
                         
        {hbold("Logo logo você recebera o link de acesso ao Grupo VIP 🔥")}""")
    photo_file_id = message.photo[-1].file_id
    
    chatid = -1001687693333
    await bot.send_message(chat_id=chatid, text=f"""Nova Solicitação de Compra
                           
            Dados Do Usuario Abaixo Da Foto
            {hbold("Chave Pix: CHAVE PIX PLACEHOLDER")}""")
    await bot.send_photo(chat_id=chatid, photo=photo_file_id)
    await bot.send_message(chat_id=chatid, text=f""".        
            Nome:       {hbold(message.chat.first_name)}
            Sobrenome:  {hbold(message.chat.last_name)}
            Usuário:    {hbold(message.chat.username)}
            Message Id: {hbold(message.message_id)}
            Chat Id:    {hbold((message.chat.id))}
            
                        """)
    await bot.send_message(chat_id=chatid, text="------------------------------- FIM DA SOLICITAÇÃO -------------------------------")
    await state.clear()
    
    
    
@dp.message(Form.comprovante)
async def process_unknown_message(message: Message, state: FSMContext) -> None:
    await message.reply("Isso não é uma imagem 😢 Digite /start para começar novamente")
    await state.clear()
    

    









#######################################################
################## SERVER REQUEST #####################
#######################################################




@dp.message(F.text == ("/acesso"), F.chat.func(lambda chat: chat.id == -1001687693333))
async def admin_acesso_chatid(message: Message, state: FSMContext):

    await state.set_state(Form.compchatid)
    await message.answer("Digite o Id do Chat:")
    
    
@dp.message(Form.compchatid)
async def admin_acesso_link(message: Message, state: FSMContext):
    await state.update_data(compchatid=message.text)
    global chatid_user_acesso
    chatid_user_acesso = message.text
    await state.clear()
    await message.answer("Agora o Link de Acesso ÚNICO: ")
    await state.set_state(Form.complinkacesso)

@dp.message(Form.complinkacesso)
async def admin_envio_acesso(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(complinkacesso=message.text)
    await state.clear()
    linkacesso_user = message.text
    await bot.send_message(chat_id=chatid_user_acesso, text=f"""Oi de novo 😜 
Só vim te avisar que seu pedido foi 🎉 APROVADO 🎉
                
    {hbold("Seu Link de Acesso:", linkacesso_user)} """)
    await message.answer("Mensagem Enviava Com Sucesso")
    #print(chatid_user_acesso, linkacesso_user) #DEBUG DEBUG













@dp.message(F.chat.func(lambda chat: chat.type == "private"))
async def echo_handler(message: types.Message) -> None:
    try:
        await message.answer("Digite /start para começar.")
    except TypeError:
        await message.answer("O que é isso?")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())