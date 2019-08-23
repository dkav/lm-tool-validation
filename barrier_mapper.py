class ToolValidator:
    """Class for validating a tool's parameter values and controlling
    the behavior of the tool's dialog."""

    def __init__(self):
        """Setup the Geoprocessor and the list of tool parameters."""
        import arcgisscripting as ARC        
        self.GP = ARC.create(9.3)
        self.params = self.GP.getparameterinfo()

    def initializeParameters(self):
        """Refine the properties of a tool's parameters.  This method is
        called when the tool is opened."""

        return

    def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parmater
        has been changed."""

        return

    def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        # Project dir validation
        if not self.params[0].HasError() and self.params[0].Altered:
            if (len(str(self.params[0].value)) > 100) or (
                set("# ").intersection(str(self.params[0].value))):
                self.params[0].SetErrorMessage("Project directory must be less"
                                               " than 100 characters in length"
                                               " and must not contain spaces.")       

       # Allow empty entry for step value when just 1 radius entered
        if not self.params[3].value:
                self.params[4].ClearMessage()
        if self.params[2].value == self.params[3].value:
                self.params[4].ClearMessage()
                
        return

