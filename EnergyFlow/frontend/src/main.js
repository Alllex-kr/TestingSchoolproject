import {createApp} from 'vue';
import {createPinia} from 'pinia';
import PrimeVue from 'primevue/config';

import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Toast from 'primevue/toast';
import Slider from 'primevue/slider'
import Dialog from 'primevue/dialog';


import 'primevue/resources/themes/bootstrap4-light-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';


import App from './App.vue';
import router from './router';
import './index.css';

const app = createApp(App);

app.use(PrimeVue);
app.use(createPinia());
app.use(router);

app.component('InputText', InputText);
app.component('Button', Button);
app.component('Toast', Toast);
app.component('Slider', Slider);
app.component('Dialog', Dialog);


app.mount('#app');
