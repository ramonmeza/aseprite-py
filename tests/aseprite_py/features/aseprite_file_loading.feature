Feature: Aseprite File Loading

    Support the loading of Aseprite files: *.ase/*.asesprite

    Scenario: File Header Loading
        Given the Aseprite object is loaded
         When we access the header attributes
         Then the header attributes are loaded
