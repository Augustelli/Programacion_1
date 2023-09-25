import { Component } from '@angular/core';
import { Input } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-abm',
  templateUrl: './abm.component.html',
  styleUrls: ['./abm.component.css']
})
export class AbmComponent {
  @Input() user_id!: string;
  @Input() tipoOperacion!: string;

  constructor(private router: Router) {}

  back() {
    this.router.navigate(['/usuarios']);
}
}
