import * as express from "express";
import { generalErrorHandler } from "@src/middlewares/error-handler";
import router from "@src/routes";

const PORT = 3000;

const app = express();

app.use(express.static(__dirname + "/views"));

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(router);

app.use(generalErrorHandler);

app.listen(PORT, () => {
  console.log(`server is running on port ${PORT}`);
});
