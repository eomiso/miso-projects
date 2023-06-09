import * as express from 'express';

// type ErrorHandler = (err: Error, req: express.Request, res: express.Response, next: express.NextFunction) => void;

const generalErrorHandler = (err: Error, req: express.Request, res: express.Response, next: express.NextFunction) => {
  if (err) {
    res.status(500).send({message: err.message, status: 500});
  }
  next();
};

export default generalErrorHandler;
