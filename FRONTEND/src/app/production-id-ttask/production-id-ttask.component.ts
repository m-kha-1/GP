import { Component,Input } from '@angular/core';
import { Task } from '../production/task_in';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-production-id-ttask',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './production-id-ttask.component.html',
  styleUrl: './production-id-ttask.component.css'
})
export class ProductionIdTtaskComponent {

  @Input() task: {tasks:Task[]} | null = null;

}
 