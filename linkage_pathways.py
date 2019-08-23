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

        # Disable optional parameters when not required
        if self.params[8].value or self.params[4].value:
            self.params[17].Enabled = True
        else:
            self.params[17].Enabled = False
        if (self.params[8].value or self.params[10].value
            or self.params[14].value):
            self.params[18].Enabled = True
        else:
            self.params[18].Enabled = False
        if (self.params[5].value or self.params[8].value
            or self.params[10].value or self.params[14].value):
            self.params[19].Enabled = True
        else:
            self.params[19].Enabled = False

        # Step 1

        # Step 2
        if self.params[5].value:
            self.params[7].Enabled = True           
            self.params[6].Enabled = True
        else:
            self.params[7].Enabled = False     
            self.params[6].Enabled = False

        # Step 3
        if self.params[8].value:
            self.params[9].Enabled = True
        else:
            self.params[9].Enabled = False

        # Step 4
        if self.params[10].value:
            self.params[11].Enabled = True
            self.params[12].Enabled = True
            self.params[13].Enabled = True
        else:
            self.params[11].Enabled = False
            self.params[12].Enabled = False
            self.params[13].Enabled = False

        # Step 5
        if self.params[14].value:
            self.params[15].Enabled = True
            if self.params[15].value:
                self.params[16].Enabled = True
            else:
                self.params[16].Enabled = False
        else:
            self.params[15].Enabled = False
            self.params[16].Enabled = False

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

        # Allow confor file to empty when step 2 is skipped
        if not self.params[5].value or self.GP.ProductInfo() == "ArcInfo":
                self.params[7].ClearMessage()

        # Check for skipped steps
        msg = ("You can start or stop at different steps, but you can't "
                   "skip any except for step 4.")
        if (self.params[4].value and not self.params[5].value and
            (self.params[8].value or self.params[10].value or self.params[14].value)):
            self.params[5].SetErrorMessage(msg)
        if (self.params[4].value or self.params[5].value) and not self.params[8].value and (
            self.params[10].value or self.params[14].value):
            self.params[8].SetErrorMessage(msg)

        return


