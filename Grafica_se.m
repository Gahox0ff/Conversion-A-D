% Extraer tiempo y voltaje
t = DATOS1.Tiempo_ms;
V = DATOS1.Voltaje_V;

figure;
plot(t, V); 
xlabel('Tiempo (s)');
ylabel('Voltaje (V)');
title('Señal adquirida - Muestreo a 20 Hz');
grid on;
legend('Datos muestreados');

figure;
plot(t, V);
xlabel('Tiempo (s)');
ylabel('Voltaje (V)');
title('señal');
grid on;
xlim([0 150]); %Limnitar el numero de ciclos para visualizar la onda
