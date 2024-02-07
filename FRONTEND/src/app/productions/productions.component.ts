import { Component,OnInit } from '@angular/core';

import { ProductionComponent } from '../production/production.component';
import { ProductionIdTtaskComponent } from '../production-id-ttask/production-id-ttask.component';

import { ProductionsService } from '../productions.service';
import { CommonModule } from '@angular/common';

import { NgFor } from '@angular/common';

import { RouterOutlet } from '@angular/router';
import { ComponentCommunicatorService } from '../component-communicator-service.service';
import { RouterLink } from '@angular/router';
 


@Component({
  selector: 'app-productions',
  standalone: true,
  imports: [ProductionComponent,ProductionIdTtaskComponent,CommonModule,RouterOutlet,RouterLink],
  templateUrl: './productions.component.html',
  styleUrl: './productions.component.css'
})
export class ProductionsComponent implements OnInit {

 
  // productions:any=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'];

  productions: any;
  tasks: any[] = [];

  constructor(private productionService: ProductionsService,private componentCommunicatorService: ComponentCommunicatorService ) { }
  ngOnInit() :void{this.loadProductions();
    }
   
    loadProductions(){this.productionService.getProductions().subscribe((data: any) => {
      this.productions = data;
      console.log(this.productions)
  })

  }
    
    
  // onEventClick(event:any):void{this.productionService.loadTasksByProductionId(event['id']).subscribe((d: any) => {
  //   this.tasks = d.tasks; });console.log(this.tasks[0]);this.componentCommunicatorService.setData(this.tasks); }
    onEventClick(event:any):void{this.componentCommunicatorService.setData(event); }
  //affiche le tavbleau
    // console.log(this.tasks)
}


// onEventClick(event:any){console.log(event['id'])}
