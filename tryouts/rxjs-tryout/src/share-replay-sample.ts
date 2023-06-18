import { Subject, ReplaySubject, of, interval, merge } from "rxjs";
import { map, mergeAll, scan, share, shareReplay } from "rxjs/operators";
import * as process from "process";

(() => {
  try {
    if (process.argv[2] === "-share") {
      (() => {
        const routeEnd = new Subject<{ data: any; url: string }>();

        const lastUrl = routeEnd.pipe(
          map((route) => route?.url),
          share()
        );

        const initialSubscriber = lastUrl.subscribe(console.log);

        routeEnd.next({ data: {}, url: "my-path" });

        // This subscriber will not receive the last value
        const lateSubscriber = lastUrl.subscribe(console.log);
      })();

      return;
    }

    if (process.argv[2] === "-shareReplay") {
      () => {
        const routeEnd = new Subject<{ data: any; url: string }>();

        const lastUrl = routeEnd.pipe(
          map((route) => route?.url),
          shareReplay(2)
        );

        const initialSubscriber = lastUrl.subscribe(console.log);

        routeEnd.next({ data: {}, url: "my-path" });

        // This subscriber will receive the last value
        const lateSubscriber = lastUrl.subscribe(console.log);
      };

      return;
    }

    if (process.argv[2] === "-ReplaySubject") {
      (() => {
        const routeEnd = new ReplaySubject<{ data: any; url: string }>(1);

        const lastUrl = routeEnd.pipe(map((route) => route?.url));

        const initialSubscriber = lastUrl.subscribe(console.log);

        routeEnd.next({ data: {}, url: "my-path" });

        // This subscriber will receive the last value
        const lateSubscriber = lastUrl.subscribe(console.log);

        return;
      })();
    }

    if (process.argv[2] === "-accumulateSource") {
      (() => {
        const observable = of([1], [2, 3], [4, 5]);

        console.log("scan");

        const subscription = observable
          .pipe(
            scan((acc, value) => {
              return [...acc, ...value];
            })
          )
          .subscribe((value) => console.log(value));
      })();

      return;
    }

    if (process.argv[2] === "-merge") {
      console.log("merge");

      (() => {
        //emit every 2.5 seconds
        const first = interval(2500);
        //emit every 1 second
        const second = interval(1000);
        //used as instance method
        const example = merge(first, second);
        //output: 0,1,0,2....
        const subscribe = example.subscribe((val) => console.log(val));
      })();

      return;
    }

    throw new Error(`${process.argv[2]} is not a valid argument. Valid arguments are:
        -share
        -shareReplay
        -ReplaySubject
        -accumulateSource
        -merge
      `);
  } catch (error) {
    if (error instanceof Error) console.error(error.message);
  }
})();
