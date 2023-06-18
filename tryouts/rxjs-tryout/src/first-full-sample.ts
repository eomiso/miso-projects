import { of } from 'rxjs';
import { tap, map, filter, debounce } from 'rxjs/operators';

const dataSource = of(1, 2, 3, 4, 5);

const subscription = dataSource
  .pipe(
    debounce(() => of(1000)),
    map(value => value * 2),
    tap(value => console.log(value)),
    filter(value => value > 5),
    tap(value => console.log(value)),
  )
  .subscribe(value => console.log(value));
