import ninja
import pets

devin = ninja.Ninja('devin', 'lozano', 'bones', 'kibble', pet=pets.Pet('spot', 'dog', 'fetch'))
devin.feed().walk().bathe()
