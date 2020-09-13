# Build Network and Map Linkages

import arcpy


class ToolValidator(object):
    """Class for validating a tool's parameter values and controlling
    the behavior of the tool's dialog."""

    def __init__(self):
        """Setup arcpy and the list of tool parameters."""
        self.params = arcpy.GetParameterInfo()

    def initializeParameters(self):
        """Refine the properties of a tool's parameters.
        This method is called when the tool is opened."""

    def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed. This method is called whenever a parameter
        has been changed."""
        # Disable optional parameters when not required
        if self.params[8].value or self.params[4].value:
            self.params[17].enabled = True
        else:
            self.params[17].enabled = False
        if (self.params[8].value or self.params[10].value
                or self.params[14].value):
            self.params[18].enabled = True
        else:
            self.params[18].enabled = False
        if (self.params[5].value or self.params[8].value
                or self.params[10].value or self.params[14].value):
            self.params[19].enabled = True
        else:
            self.params[19].enabled = False

        # Step 1

        # Step 2
        if self.params[5].value:
            self.params[7].enabled = True
            self.params[6].enabled = True
        else:
            self.params[7].enabled = False
            self.params[6].enabled = False

        # Step 3
        if self.params[8].value:
            self.params[9].enabled = True
        else:
            self.params[9].enabled = False

        # Step 4
        if self.params[10].value:
            self.params[11].enabled = True
            self.params[12].enabled = True
            self.params[13].enabled = True
        else:
            self.params[11].enabled = False
            self.params[12].enabled = False
            self.params[13].enabled = False

        # Step 5
        if self.params[14].value:
            self.params[15].enabled = True
            if self.params[15].value:
                self.params[16].enabled = True
            else:
                self.params[16].enabled = False
        else:
            self.params[15].enabled = False
            self.params[16].enabled = False

    def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        # Project dir validation
        if not self.params[0].hasError() and self.params[0].altered:
            if (len(str(self.params[0].value)) > 100 or
                    set("# ").intersection(str(self.params[0].value))):
                self.params[0].setErrorMessage("Project directory must be less"
                                               " than 100 characters in length"
                                               " and must not contain spaces.")

        # Allow confor file to empty when step 2 is skipped
        if not self.params[5].value or arcpy.ProductInfo() == "ArcInfo":
            self.params[7].clearMessage()

        # Check for skipped steps
        msg = ("You can start or stop at different steps, but you can't "
               "skip any except for step 4.")
        if (self.params[4].value and not self.params[5].value and
                (self.params[8].value or self.params[10].value or
                 self.params[14].value)):
            self.params[5].setErrorMessage(msg)
        if ((self.params[4].value or self.params[5].value) and
                not self.params[8].value and
                (self.params[10].value or self.params[14].value)):
            self.params[8].setErrorMessage(msg)

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True
