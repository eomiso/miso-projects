import * as fs from "fs";
import * as express from "express";
import Calculator from "@src/models";

class Controller {
  public router = express.Router();
  public path: string;

  constructor(path: string) {
    this.path = path;
  }

  mainView(req: express.Request, res: express.Response) {
    const calc = new Calculator(1, 2);
    console.log(calc.sum());

    fs.readFile("./src/views/index.html", "utf-8", (err, data) => {
      res.send(data);
    });
  }
}

const controller = new Controller("/main");

export default controller;
