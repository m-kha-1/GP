import { Component, Input,Output,EventEmitter } from '@angular/core';
import { Production } from './production_in';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router'



@Component({
  selector: 'app-production',
  standalone: true,
  imports: [CommonModule,RouterModule],
  templateUrl: './production.component.html',
  styleUrl: './production.component.css'
})
export class ProductionComponent {

  @Input() production: Production | null = null;
  
  @Output()  monevenement:EventEmitter<any> = new EventEmitter();

  onClick(){
    this.monevenement.emit(this.production?.id);
    console.log(this.production?.id+"  catché", typeof(this.production?.id));
    // this.monevenement.emit([this.production?.id,this.production?.name]);

  }
  




  
}
