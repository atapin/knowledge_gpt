# flake8: noqa
from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """Дай окончательный ответ на заданные вопросы, используя предоставленные выдержки из документов (в произвольном порядке) в качестве ссылок. ВСЕГДА включайте в свой ответ раздел «ИСТОЧНИКИ», включающий только минимальный набор источников, необходимый для ответа на вопрос. Если вы не можете ответить на вопрос, просто скажите, что вы не знаете. Не пытайтесь сфабриковать ответ и оставьте раздел ИСТОЧНИКИ пустым.

---------

ВОПРОС: Какова цель ARPA-H?
=========
Содержание: Больше поддержки пациентам и их семьям. \n\nДля достижения этой цели я призываю Конгресс профинансировать ARPA-H, Агентство перспективных исследовательских проектов в области здравоохранения. \n\nОн основан на DARPA — проекте Министерства обороны, который привел к созданию Интернета, GPS и многого другого. \n\nARPA-H будет иметь единственную цель — добиться прорыва в лечении рака, болезни Альцгеймера, диабета и многого другого.
Источник: 1-32
Содержание: Раз уж мы этим занимаемся, давайте позаботимся о том, чтобы каждый американец мог получить необходимую ему медицинскую помощь. \n\nМы уже сделали исторические инвестиции в здравоохранение. \n\nМы упростили американцам получение необходимой им помощи, когда она им нужна. \n\nМы упростили американцам получение необходимого им лечения тогда, когда оно им необходимо. \n\nМы упростили американцам получение необходимых им лекарств, когда они им нужны.
Источник: 1-33
Содержание: В.А. разрабатывает новые способы связи токсического воздействия с болезнями, уже помогая ветеранам получить помощь, которую они заслуживают. \n\nМы должны оказать такую же заботу всем американцам. \n\nВот почему я призываю Конгресс принять закон, который учредит национальный реестр токсичных воздействий и предоставит медицинскую и финансовую помощь пострадавшим.
Источник: 1-30
=========
ОТВЕТ: Цель ARPA-H — добиться прорыва в лечении рака, болезни Альцгеймера, диабета и т. д.
ИСТОЧНИКИ: 1-32.

---------

ВОПРОС: {question}
=========
{summaries}
=========
ОТВЕТ:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
