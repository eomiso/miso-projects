import { Request, Response, NextFunction } from "express";

const generalErrorHandler = (
  err: Error,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  if (err) {
    console.log(err.message); // FIXME: Use winston logger
  }
  next(err);
};

export { generalErrorHandler };
