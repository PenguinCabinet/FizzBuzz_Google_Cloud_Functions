# 👏FizzBuzz Google Cloud Functions
Google Cloud Functionsで動くFizzBuzz判定APIです。

## 🏗デプロイ
```bash
make deploy
```

## 🔨使い方

$(url)はデプロイ先のURLです。


```bash
>curl $(url)/CheckFizzBuzz?n=15 
FizzBuzz
```

```bash
>curl $(url)/CheckFizzBuzz?n=6
6 
```

```bash
>curl $(url)/CheckFizzBuzz?n=Hello
ERROR:n is not number 
```

## 🎫LICENSE

[MIT](./LICENSE)

## ✍Author

[PenguinCabinet](https://github.com/PenguinCabinet)