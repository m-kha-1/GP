import { Component,OnInit
 } from '@angular/core';
import { ProductionsService } from '../productions.service';
import { CommonModule } from '@angular/common';
import { FormsModule} from '@angular/forms';


// Classe représentant un producteur
class Producer {
  id: number;
  name: string;
  selected: boolean;

  constructor(id: number, name: string) {
    this.id = id;
    this.name = name;
    this.selected = false; // Par défaut, la case à cocher n'est pas cochée
  }
}


@Component({
  selector: 'app-addform',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './addform.component.html',
  styleUrl: './addform.component.css'
})
export class AddformComponent  implements OnInit {

  producer: Producer[]=[]
  
  //variable prenant les différents producteurs disponibles
  producerList: any 
  
 
  

  
  formData={
  
    name:"",
    client:"",
    producers:[] as number[]
   
  }
  constructor(private productionsService: ProductionsService){}
  ngOnInit(): void {this.loadProducer()}
 

  loadProducer(){
    this.producerList=this.productionsService.loadProducer().subscribe((data:any) => this.producerList=data);console.log(this.producerList);   
  }
  submitForm(){
    // this.formData.producers=this.formData.producers.map(Number)
     
     this.productionsService.createNewProduction(this.formData).subscribe(
     );console.log(this.formData)
  }
  updateSelectedProducers(): void {
    this.formData.producers = this.producerList.filter((producer: Producer) => producer.selected).map((producer: Producer) => producer.id);
    console.log(this.formData)
  }
}

