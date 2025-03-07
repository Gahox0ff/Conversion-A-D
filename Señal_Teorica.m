% Parámetros
A = 1.4;           % Amplitud (Vpp / 2)
DC = 1.5;          % Componente DC
f = 20;            % Frecuencia en Hz
t = 0:0.001:1;     % Vector de tiempo (de 0 a 1 segundo con intervalo de 1 ms)

% Señal seno con componente DC
y = A * sin(2 * pi * f * t) + DC;

% Graficar la señal
figure;
plot(t, y);
title('Señal Senoidal con Componente DC');
xlabel('Tiempo (s)');
ylabel('Amplitud (V)');
xlim ([0 0.08])
grid on;
