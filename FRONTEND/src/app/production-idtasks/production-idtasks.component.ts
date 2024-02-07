import { Component,OnInit } from '@angular/core';
import { ComponentCommunicatorService } from '../component-communicator-service.service';
import { ProductionsService } from '../productions.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-production-idtasks',
  standalone: true,
  imports: [CommonModule],
  providers:[ProductionsService],
  templateUrl: './production-idtasks.component.html',
  styleUrl: './production-idtasks.component.css'
})
export class ProductionIdtasksComponent {
  sharedData: any;
  productionIdTasks:any
  constructor(private  componentCommunicatorService: ComponentCommunicatorService,private productionsService:ProductionsService){}
  ngOnInit(): void{
    this.sharedData =this.componentCommunicatorService.getData();
    console.log(this.sharedData)
    this.productionsService.loadTasksByProductionId(this.sharedData).subscribe((data:any) =>{this.productionIdTasks = data});
    console.log(this.productionIdTasks)
    
  }
  
}
