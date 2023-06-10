import * as express from "express";
import controller from "./controller";

const router = express.Router();

router.get(controller.path, controller.mainView);

export default router;
