import * as express from "express";
import generalErrorHandler from "./middlewares/general-error-handler";

const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/", (req, res) => {
  res.status(200).send({ message: "ok" });
});

app.post("/hello", (req, res) => {
  const { name } = req.body;

  if (!name) {
    throw new Error("POST /hello: name is required");
  }

  res.status(200).send({ message: `hello ${name}` });
});

app.use(
  (
    err: Error,
    req: express.Request,
    res: express.Response,
    next: express.NextFunction
  ) => {
    if (err) {
      console.log(err.message);
    }
    next(err);
  }
);

app.use(generalErrorHandler);

app.listen(3000, () => {
  console.log("server is running on port 3000");
});
