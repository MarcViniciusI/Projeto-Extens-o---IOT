# 🌡️ Projeto de Monitoramento de Temperatura para Secadoras Industriais 🌪️

O que é isso? 🤔
Essa é a aplicação dos sonhos para quem quer evitar que suas secadoras industriais passem do limite! 🚨

Imagina só: uma secadora com sensores IoT que monitoram a temperatura em tempo real, mandam os dados para a nuvem, e ainda te avisam no Telegram se a temperatura estiver prestes a queimar tudo! Isso mesmo, aqui a gente joga seguro para evitar surpresas (e roupas queimadas!).

Por que isso é importante? 💡
Secadoras industriais são maravilhosas para grandes volumes de roupa, mas, se esquentam demais... 💥 os prejuízos podem ser grandes! Queimaduras em tecidos e até danos ao equipamento. E não queremos isso, certo?

Esse projeto foi desenvolvido justamente para manutenção preditiva, garantindo que você saiba exatamente quando as coisas estão esquentando mais do que deveriam e tomar providências antes que os problemas aconteçam.

###  Funcionalidades 🔥
Monitoramento em tempo real das temperaturas de uma secadora industrial.
Alertas automáticos no Telegram quando a temperatura passar de um certo limite (olha o alerta de 94°C aí!).
Histórico de temperaturas disponível via interface web, para você visualizar e analisar as variações.
Integração com Firebase para armazenamento e análise de dados.
MQTT para comunicação rápida e eficiente dos dados dos sensores.

### Tecnologias Usadas 💻
Python 🐍: O cérebro da operação, controlando o backend.

Flask 🌐: Framework web para a interface e o painel de monitoramento.

MQTT 📡: Para a comunicação dos dados entre o sensor e o servidor.

Firebase 🔥: Para armazenar os dados e garantir que você nunca perca um registro de temperatura.

Telegram Bot API 🤖: Porque receber mensagens de alerta no Telegram é muito mais prático do que ter que ficar de olho no termômetro o dia todo!

Plotly 📊: Para criar gráficos interativos e bonitos no painel de histórico.

###  Como isso tudo funciona? 🚀
Monitoramento: A secadora está equipada com sensores que capturam a temperatura ambiente e mandam esses dados para o servidor via MQTT.
Alerta: Quando a temperatura passa dos 94°C, o servidor envia uma mensagem automática para o Telegram com um alerta urgente.
Histórico: Toda a coleta de dados é armazenada no Firebase e pode ser acessada a qualquer momento pelo painel web. Você pode ver todos os registros e analisar os dados para melhorar a operação.

##  LOGIN
![login](https://github.com/user-attachments/assets/09fcec3e-c5fd-4fdc-9f61-1ffba024841e)
##  DASHBOARD 
![dashboard](https://github.com/user-attachments/assets/a0fdae23-e7c5-46b5-a198-a9356f716014)
##  HISTORICO
![historico](https://github.com/user-attachments/assets/31d174e1-71ec-4fb6-98da-ee15d4e64c26)
##  INSIGHTS
![insights](https://github.com/user-attachments/assets/c6035f32-2650-4fb8-8cc7-6001221bf06e)
## TELEGRAM
![telegram](https://github.com/user-attachments/assets/4fdd3340-573d-42ce-8982-1795b560b02a)



###  Conclusão 🎉
Esse projeto foi criado com o objetivo de aplicar conhecimento teórico na prática e resolver um problema real. Espero que você curta explorar e utilizar essa aplicação tanto quanto eu curti desenvolvê-la!
Se você se preocupava com roupas queimadas na secadora, agora pode ficar tranquilo! 😎
