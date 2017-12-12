#include <Softwarebt.h>
#include <PinChangeInt.h>
#include <PinChangeIntConfig.h>
#include <eHealth.h>
#include <eHealthDisplay.h>

char serialByte;
uint8_t state = 0;
uint8_t cont = 0;
SoftwareSerial bt(10,11);

    void setup()
    {
        eHealth.readGlucometer();
	bt.begin(9600);
        pinMode(2,OUTPUT)
        digitalWrite(2,HIGH)
        initScreen();
        delay(100);
    }

    void loop()
    {
      state = 0;

       while (bt.available()>0){
        serialByte=bt.read();

          if ((serialByte=='A') || (serialByte == 'a')){ //Airflow sensor
            airFlowMenu();
            airFlowBucle();

          } else if ((serialByte=='S') || (serialByte == 's')){
            skinSensorMenu();
            skinSensorBucle();

          } else if ((serialByte=='E') || (serialByte == 'e')){
            ECGMenu();
            ECGBucle();

          } else if ((serialByte=='P') || (serialByte == 'p')){
            pulsioximeterMenu();
            pulsioximeterBucle();

          } else if ((serialByte=='B') || (serialByte == 'b')){
            bodyPositionMenu();
            bodyPositionBucle();

          } else if ((serialByte=='T') || (serialByte == 't')){
            temperatureMenu();
            temperatureBucle();

          } else if ((serialByte=='N') || (serialByte == 'n')){
            GlucometerMenu();
            GlucometerBucle();
          }
       }
    }

//=================================================================================================================
//=================================================================================================================
    void initScreen(void)
    {
      printLogoEhealth();
      delay(100);
      mainMenu();
    }
//=================================================================================================================
//=================================================================================================================
    void mainMenu(void)
    {
       lineFeed();  bt.print(F("  --------> EHEALTH MENU OPTIONS <--------"));  lineFeed();  lineFeed();

       initialSpace();   bt.print(F("A : AirFlow sensor options"));       lineFeed();
       initialSpace();   bt.print(F("S : Skin sensor options"));          lineFeed();
       initialSpace();   bt.print(F("E : ECG sensor options"));           lineFeed();
       initialSpace();   bt.print(F("P : Pulsioximeter sensor options")); lineFeed();
       initialSpace();   bt.print(F("B : Body position sensor options")); lineFeed();
       initialSpace();   bt.print(F("T : Temperature sensor options"));   lineFeed();
       initialSpace();   bt.print(F("N : Glucometer sensor options"));lineFeed();
    }
//=================================================================================================================
//=================================================================================================================
    void airFlowMenu(void)
    {
      lineFeed();      bt.print(F("--------> AIRFLOW MENU OPTIONS <--------"));  lineFeed();  lineFeed();
      initialSpace();  bt.print(F("W : Wave form"));  lineFeed();
      initialSpace();  bt.print(F("V : Analogic value"));  lineFeed();
      initialSpace();  bt.print(F("B : BACK MAIN MENU"));  lineFeed();
    }
//=================================================================================================================
//=================================================================================================================
    void airFlowBucle(void) {
      while (state == 0) {
        while (bt.available()>0){
          serialByte=bt.read();
             if ((serialByte=='W') || (serialByte == 'w')){ //Airflow sensor
                while(1){
                  serialByte=bt.read();
                  eHealth.airFlowWave(eHealth.getAirFlow());

                  if ((serialByte== 'B') || (serialByte == 'b')) {
                    airFlowMenu();
                    break;
                  }
                }
              } else if ((serialByte=='V') || (serialByte == 'v')){
                  while(1){
                    serialByte=bt.read();
                    bt.print(F(" Airflow analogic value : "));
                    bt.println(eHealth.getAirFlow());
                    delay(20);
                       if ((serialByte== 'B') || (serialByte == 'b')) {
                         airFlowMenu();
                         break;
                       }
                  }
              } else if ((serialByte=='B') || (serialByte == 'b')){
                state = 1;
              }
           }
        }
      mainMenu();
    }
//=================================================================================================================
//=================================================================================================================
    void skinSensorMenu(void)
    {
      lineFeed();      bt.print(F("--------> SKIN SENSOR MENU OPTIONS <--------"));  lineFeed();  lineFeed();
      outputMenu();
    }
//=================================================================================================================
//=================================================================================================================
    void skinSensorBucle(void) {
      while (state == 0) {
          while (bt.available()>0){
            serialByte=bt.read();
               if ((serialByte=='S') || (serialByte == 's')){
                  while(1){

                    lineFeed();

                    serialByte=bt.read();
                    float conductance = eHealth.getSkinConductance();
                    long resistance = eHealth.getSkinResistance();
                    float conductanceVoltage = eHealth.getSkinConductanceVoltage();

                     if (conductance == -1) {
                       bt.println(" No patient connection");
                     } else {

                       bt.print(F(" Skin conductance value : "));
                       bt.println(conductance);

                       bt.print(F(" Skin resistance value : "));
                       bt.println(resistance);

                       bt.print(F(" Skin conductance value in volts: "));
                       bt.println(conductanceVoltage);

                       delay(500);
                     }

                    if ((serialByte== 'B') || (serialByte == 'b')) {
                      skinSensorMenu();
                      break;
                    }
                  }


                } else if ((serialByte=='B') || (serialByte == 'b')){
                  state = 1;
                }
             }
          }
        mainMenu();
    }
//=================================================================================================================
//=================================================================================================================
    void ECGMenu(void) {
      lineFeed();  bt.print(F("--------> ECG MENU OPTIONS <--------"));  lineFeed();  lineFeed();
      outputMenu();
    }
//=================================================================================================================
//=================================================================================================================
    void ECGBucle(void) {
        while (state == 0) {
          while (bt.available()>0){
            serialByte=bt.read();
               if ((serialByte=='S') || (serialByte == 's')){
                  while(1){

                    lineFeed();
                    serialByte=bt.read();

                    delay(500);

                    if ((serialByte== 'B') || (serialByte == 'b')) {
                      ECGMenu();
                      break;
                    }
                  }
                } else if ((serialByte=='B') || (serialByte == 'b')){
                  state = 1;
                }
             }
          }
        mainMenu();
    }
//=================================================================================================================
//=================================================================================================================
    void pulsioximeterMenu(void)
    {
      lineFeed();      bt.print(F("--------> PULSIOXIMETER MENU OPTIONS <--------"));  lineFeed();  lineFeed();
      outputMenu();
    }
//=================================================================================================================
//=================================================================================================================
    void pulsioximeterBucle(void)
    {
        //Attach the interruptions for using the pulsioximeter.
        PCintPort::attachInterrupt(6, readPulsioximeter, RISING);
        eHealth.initPulsioximeter();

        while (state == 0) {
          while (bt.available()>0){
            serialByte=bt.read();
               if ((serialByte=='S') || (serialByte == 's')){
                  while(1){

                    //eHealth.readPulsioximeter();

                    lineFeed();
                    serialByte=bt.read();
                    bt.print("PRbpm : ");
                    bt.print(eHealth.getOxygenSaturation());

                    bt.print(" % SPo2 : ");
                    bt.print(eHealth.getBPM());

                    bt.print("\n");
                    delay(500);

                    if ((serialByte== 'B') || (serialByte == 'b')) {
                      pulsioximeterMenu();
                      break;
                    }
                  }
                } else if ((serialByte=='B') || (serialByte == 'b')){
                  state = 1;
                }
             }
          }
        mainMenu();

        PCintPort::detachInterrupt(6);
    }
//=================================================================================================================
//=================================================================================================================
    void bodyPositionMenu(void)
    {
      lineFeed();  bt.print(F("--------> BODY POSTITIONMENU OPTIONS <--------"));  lineFeed();  lineFeed();
      outputMenu();
    }
//=================================================================================================================
//=================================================================================================================
    void bodyPositionBucle(void)
    {
       while (state == 0) {
          while (bt.available()>0){

            eHealth.initPositionSensor();
            serialByte=bt.read();
               if ((serialByte=='S') || (serialByte == 's')){
                  while(1){

                    lineFeed();
                    serialByte=bt.read();

                    bt.print("Current position : ");
                    uint8_t position = eHealth.getBodyPosition();
                    eHealth.printPosition(position);
                    delay(100);

                    if ((serialByte== 'B') || (serialByte == 'b')) {
                      bodyPositionMenu();
                      break;
                    }
                  }
                } else if ((serialByte=='B') || (serialByte == 'b')){
                  state = 1;
                }
             }
          }
        mainMenu();
    }
//=================================================================================================================
//=================================================================================================================
    void temperatureMenu(void)
    {
      lineFeed();  bt.print(F("--------> TEMPERATURE MENU OPTIONS <--------"));  lineFeed();  lineFeed();
      outputMenu();
    }
//=================================================================================================================
//=================================================================================================================
    void temperatureBucle(void)
    {
          while (state == 0) {
          while (bt.available()>0){
            serialByte=bt.read();
               if ((serialByte=='S') || (serialByte == 's')){
                  while(1){

                    lineFeed();
                    serialByte=bt.read();

                    float temperature = eHealth.getTemperature();
                    bt.print("Temperature (ºC): ");
                    bt.println(temperature, 2);

                    delay(1000);

                    if ((serialByte== 'B') || (serialByte == 'b')) {
                      temperatureMenu();
                      break;
                    }
                  }
                } else if ((serialByte=='B') || (serialByte == 'b')){
                  state = 1;
                }
             }
          }
        mainMenu();
    }
//=================================================================================================================
//=================================================================================================================
    void GlucometerMenu(void)
    {
      lineFeed();  bt.print(F("--------> GLUCOMETER MENU OPTIONS <--------"));  lineFeed();  lineFeed();
      outputMenu();
    }
//=================================================================================================================
//=================================================================================================================

    void GlucometerBucle()
    {
          while (state == 0) {
          while (bt.available()>0){
            serialByte=bt.read();
               if ((serialByte=='S') || (serialByte == 's')){
                  while(1){

                    lineFeed();
                    serialByte=bt.read();

                    uint8_t numberOfData = eHealth.getGlucometerLength();
 		    bt.print(F("Number of measures : "));
                    bt.println(numberOfData, DEC);
 		    delay(100);


  for (int i = 0; i<numberOfData; i++) {
    // The protocol sends data in this order
    bt.println(F("=========================================="));

    bt.print(F("Measure number "));
    bt.println(i + 1);

    bt.print(F("Date -> "));
    bt.print(eHealth.glucoseDataVector[i].day);
    bt.print(F(" of "));
    bt.print(eHealth.numberToMonth(eHealth.glucoseDataVector[i].month));
    bt.print(F(" of "));
    bt.print(2000 + eHealth.glucoseDataVector[i].year);
    bt.print(F(" at "));

    if (eHealth.glucoseDataVector[i].hour < 10) {
      bt.print(0); // Only for best representation.
    }

    bt.print(eHealth.glucoseDataVector[i].hour);
    bt.print(F(":"));

    if (eHealth.glucoseDataVector[i].minutes < 10) {
      bt.print(0);// Only for best representation.
    }
    bt.print(eHealth.glucoseDataVector[i].minutes);

    if (eHealth.glucoseDataVector[i].meridian == 0xBB)
      bt.println(F(" pm"));
    else if (eHealth.glucoseDataVector[i].meridian == 0xAA)
      bt.println(F(" am"));

    bt.print(F("Glucose value : "));
    bt.print(eHealth.glucoseDataVector[i].glucose);
    bt.println(F(" mg/dL"));
  }

  delay(1000);

                    if ((serialByte== 'B') || (serialByte == 'b')) {
                      GlucometerMenu();
                      break;
                    }
                  }
                } else if ((serialByte=='B') || (serialByte == 'b')){
                  state = 1;
                }
             }
          }
        mainMenu();
    }



//=================================================================================================================
//=================================================================================================================
    void outputMenu(void) {
        initialSpace();  bt.print(F("S : Serial output value"));  lineFeed();
        initialSpace();  bt.print(F("B : BACK MAIN MENU"));  lineFeed();
    }

//=================================================================================================================
//=================================================================================================================
    void printLogoEhealth(void)
    {
      starLine();
      starPrint();  blank();        HLeterOne();    blank();       blank();         blank();         tLeterOne();   hLeterOne();  starPrint();   lineFeed();
      starPrint();  eLeterTwo();    HLeterTwo();    eLeterTwo();   aLeterTwo();     lLeterTwo();     tLeterTwo();   hLeterTwo();  starPrint();   lineFeed();
      starPrint();  eLeterThree();  HLeterThree();  eLeterThree(); aLeterThree();   lLeterThree();   tLeterThree(); hLeterThree();  starPrint();   lineFeed();
      starPrint();  eLeterFour();   HLeterFour();   eLeterFour();  aLeterFour();    lLeterFour();    tLeterFour();  hLeterFour();  starPrint();   lineFeed();
      starPrint();  eLeterFive();   HLeterFive();   eLeterFive();  aLeterFive();    lLeterFive();    tLeterFive();  hLeterFive();  starPrint();   lineFeed();
      starPrint();  eLeterSix();    HLeterSix();    eLeterSix();   aLeterSix();     lLeterSix();     tLeterSix();   hLeterSix();  starPrint();   lineFeed();
      starLine();
    }
//=================================================================================================================
//=================================================================================================================
    void eLeterTwo(void)   { bt.print(F(" _____  "));  }
    void eLeterThree(void) { bt.print(F("|  __ | "));  }
    void eLeterFour(void)  { bt.print(F("|  ___| "));  }
    void eLeterFive(void)  { bt.print(F("| |___  "));  }
    void eLeterSix(void)   { bt.print(F("|_____| "));  }

    void HLeterOne(void)   { bt.print(F(" _    _  ")); }
    void HLeterTwo(void)   { bt.print(F("| |  | | ")); }
    void HLeterThree(void) { bt.print(F("| |__| | ")); }
    void HLeterFour(void)  { bt.print(F("|  __  | ")); }
    void HLeterFive(void)  { bt.print(F("| |  | | ")); }
    void HLeterSix(void)   { bt.print(F("|_|  |_| ")); }


    void aLeterTwo(void)   { bt.print(F(" ______  ")); }
    void aLeterThree(void) { bt.print(F("|      | ")); }
    void aLeterFour(void)  { bt.print(F("|  {}  | ")); }
    void aLeterFive(void)  { bt.print(F("|  __  | ")); }
    void aLeterSix(void)   { bt.print(F("|_|  |_| ")); }

    void lLeterTwo(void)   { bt.print(F(" _      "));  }
    void lLeterThree(void) { bt.print(F("| |     "));  }
    void lLeterFour(void)  { bt.print(F("| |     "));  }
    void lLeterFive(void)  { bt.print(F("| |____ "));  }
    void lLeterSix(void)   { bt.print(F("|______|"));  }

    void tLeterOne(void)   { bt.print(F("    _     "));}
    void tLeterTwo(void)   { bt.print(F(" _| |__  ")); }
    void tLeterThree(void) { bt.print(F("(_   __) ")); }
    void tLeterFour(void)  { bt.print(F("  | |    ")); }
    void tLeterFive(void)  { bt.print(F("  | |__  ")); }
    void tLeterSix(void)   { bt.print(F("  |____) ")); }

    void hLeterOne(void)   { bt.print(F(" _       "));}
    void hLeterTwo(void)   { bt.print(F("| |      ")); }
    void hLeterThree(void) { bt.print(F("| |___   ")); }
    void hLeterFour(void)  { bt.print(F("|  _  |  ")); }
    void hLeterFive(void)  { bt.print(F("| | | |  ")); }
    void hLeterSix(void)   { bt.print(F("|_| |_|  ")); }

//=================================================================================================================
//=================================================================================================================

    void blank(void)   { bt.print(F("        "));}

//=================================================================================================================
//=================================================================================================================
    void initialSpace(void)
    {
        bt.print(F("        "));
    }
//=================================================================================================================
//=================================================================================================================
    void starPrint(void)
    {
      bt.print(F("* "));
    }
//=================================================================================================================
//=================================================================================================================
    void lineFeed(void)
    {
      bt.print(F("\n"));
    }
//=================================================================================================================
//=================================================================================================================
    void starLine(void)
    {
      for (int i = 0; i< 63; i++)
      {
        bt.print(F("*"));
      }
      lineFeed();
    }
//=================================================================================================================
//=================================================================================================================

int freeRam () {
  extern int __heap_start, *__brkval;
  int v;
  return (int) &v - (__brkval == 0 ? (int) &__heap_start : (int) __brkval);
}

//=================================================================================================================
//=================================================================================================================

//Include always this code for using the pulsioximeter sensor
//=========================================================================
void readPulsioximeter(){

  cont ++;

  if (cont == 30) { //Get only one of 30 measures to reduce the latency
    eHealth.readPulsioximeter();
    cont = 0;
  }
}
