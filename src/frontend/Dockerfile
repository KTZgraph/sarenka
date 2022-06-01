FROM node:16.15.0-alpine3.15
# ENV NODE_VERSION 16.15.0

WORKDIR /app
RUN npm install -g npm@8.11.0
COPY package*.json ./
RUN npm install 

# app user doesn't have permission to install
# RUN addgroup app && adduser -S -G app app
# USER app

COPY . .

EXPOSE 3000

CMD ["npm", "start"]