# ./po4.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ca9a97eaf98a72b89017af3aa8f6a44b624cd71f
# Generated 2016-12-15 00:15:41.668015 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace URN:purchase-order

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:77db1992-c242-11e6-a518-0016eac6ea9c')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import address as _ImportedBinding_address
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('URN:purchase-order', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.positiveInteger):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 25, 14)
    _Documentation = None
STD_ANON._CF_maxExclusive = pyxb.binding.facets.CF_maxExclusive(value_datatype=pyxb.binding.datatypes.positiveInteger, value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON._InitializeFacetMap(STD_ANON._CF_maxExclusive)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {URN:purchase-order}SKU
class SKU (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SKU')
    _XSDLocation = pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 41, 2)
    _Documentation = None
SKU._CF_pattern = pyxb.binding.facets.CF_pattern()
SKU._CF_pattern.addPattern(pattern='\\d{3}-[A-Z]{2}')
SKU._InitializeFacetMap(SKU._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SKU', SKU)
_module_typeBindings.SKU = SKU

# Complex type {URN:purchase-order}PurchaseOrderType with content type ELEMENT_ONLY
class PurchaseOrderType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {URN:purchase-order}PurchaseOrderType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PurchaseOrderType')
    _XSDLocation = pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 9, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:purchase-order}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__URNpurchase_order_PurchaseOrderType_URNpurchase_ordercomment', False, pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 8, 2), )

    
    comment = property(__comment.value, __comment.set, None, None)

    
    # Element {URN:purchase-order}shipTo uses Python identifier shipTo
    __shipTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shipTo'), 'shipTo', '__URNpurchase_order_PurchaseOrderType_URNpurchase_ordershipTo', False, pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 11, 6), )

    
    shipTo = property(__shipTo.value, __shipTo.set, None, None)

    
    # Element {URN:purchase-order}billTo uses Python identifier billTo
    __billTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'billTo'), 'billTo', '__URNpurchase_order_PurchaseOrderType_URNpurchase_orderbillTo', False, pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 12, 6), )

    
    billTo = property(__billTo.value, __billTo.set, None, None)

    
    # Element {URN:purchase-order}items uses Python identifier items
    __items = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'items'), 'items', '__URNpurchase_order_PurchaseOrderType_URNpurchase_orderitems', False, pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 14, 6), )

    
    items = property(__items.value, __items.set, None, None)

    
    # Attribute orderDate uses Python identifier orderDate
    __orderDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'orderDate'), 'orderDate', '__URNpurchase_order_PurchaseOrderType_orderDate', pyxb.binding.datatypes.date)
    __orderDate._DeclarationLocation = pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 16, 4)
    __orderDate._UseLocation = pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 16, 4)
    
    orderDate = property(__orderDate.value, __orderDate.set, None, None)

    _ElementMap.update({
        __comment.name() : __comment,
        __shipTo.name() : __shipTo,
        __billTo.name() : __billTo,
        __items.name() : __items
    })
    _AttributeMap.update({
        __orderDate.name() : __orderDate
    })
_module_typeBindings.PurchaseOrderType = PurchaseOrderType
Namespace.addCategoryObject('typeBinding', 'PurchaseOrderType', PurchaseOrderType)


# Complex type {URN:purchase-order}Items with content type ELEMENT_ONLY
class Items (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {URN:purchase-order}Items with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Items')
    _XSDLocation = pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 18, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:purchase-order}item uses Python identifier item
    __item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'item'), 'item', '__URNpurchase_order_Items_URNpurchase_orderitem', True, pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 20, 6), )

    
    item = property(__item.value, __item.set, None, None)

    _ElementMap.update({
        __item.name() : __item
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Items = Items
Namespace.addCategoryObject('typeBinding', 'Items', Items)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 21, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {URN:purchase-order}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__URNpurchase_order_CTD_ANON_URNpurchase_ordercomment', False, pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 8, 2), )

    
    comment = property(__comment.value, __comment.set, None, None)

    
    # Element {URN:purchase-order}productName uses Python identifier productName
    __productName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productName'), 'productName', '__URNpurchase_order_CTD_ANON_URNpurchase_orderproductName', False, pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 23, 12), )

    
    productName = property(__productName.value, __productName.set, None, None)

    
    # Element {URN:purchase-order}quantity uses Python identifier quantity
    __quantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quantity'), 'quantity', '__URNpurchase_order_CTD_ANON_URNpurchase_orderquantity', False, pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 24, 12), )

    
    quantity = property(__quantity.value, __quantity.set, None, None)

    
    # Element {URN:purchase-order}USPrice uses Python identifier USPrice
    __USPrice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'USPrice'), 'USPrice', '__URNpurchase_order_CTD_ANON_URNpurchase_orderUSPrice', False, pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 31, 12), )

    
    USPrice = property(__USPrice.value, __USPrice.set, None, None)

    
    # Element {URN:purchase-order}shipDate uses Python identifier shipDate
    __shipDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shipDate'), 'shipDate', '__URNpurchase_order_CTD_ANON_URNpurchase_ordershipDate', False, pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 33, 12), )

    
    shipDate = property(__shipDate.value, __shipDate.set, None, None)

    
    # Attribute partNum uses Python identifier partNum
    __partNum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'partNum'), 'partNum', '__URNpurchase_order_CTD_ANON_partNum', _module_typeBindings.SKU, required=True)
    __partNum._DeclarationLocation = pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 35, 10)
    __partNum._UseLocation = pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 35, 10)
    
    partNum = property(__partNum.value, __partNum.set, None, None)

    _ElementMap.update({
        __comment.name() : __comment,
        __productName.name() : __productName,
        __quantity.name() : __quantity,
        __USPrice.name() : __USPrice,
        __shipDate.name() : __shipDate
    })
    _AttributeMap.update({
        __partNum.name() : __partNum
    })
_module_typeBindings.CTD_ANON = CTD_ANON


comment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 8, 2))
Namespace.addCategoryObject('elementBinding', comment.name().localName(), comment)

purchaseOrder = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'purchaseOrder'), PurchaseOrderType, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 7, 2))
Namespace.addCategoryObject('elementBinding', purchaseOrder.name().localName(), purchaseOrder)



PurchaseOrderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), pyxb.binding.datatypes.string, scope=PurchaseOrderType, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 8, 2)))

PurchaseOrderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shipTo'), _ImportedBinding_address.USAddress, scope=PurchaseOrderType, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 11, 6)))

PurchaseOrderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'billTo'), _ImportedBinding_address.USAddress, scope=PurchaseOrderType, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 12, 6)))

PurchaseOrderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'items'), Items, scope=PurchaseOrderType, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 14, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 13, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PurchaseOrderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shipTo')), pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 11, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PurchaseOrderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'billTo')), pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 12, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PurchaseOrderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 13, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PurchaseOrderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'items')), pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 14, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PurchaseOrderType._Automaton = _BuildAutomaton()




Items._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'item'), CTD_ANON, scope=Items, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 20, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 20, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Items._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'item')), pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 20, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Items._Automaton = _BuildAutomaton_()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 8, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productName'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 23, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quantity'), STD_ANON, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 24, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'USPrice'), pyxb.binding.datatypes.decimal, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 31, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shipDate'), pyxb.binding.datatypes.date, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 33, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 32, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 33, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productName')), pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 23, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quantity')), pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 24, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'USPrice')), pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 31, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 32, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shipDate')), pyxb.utils.utility.Location('/home/sergey/Py_PyXB/po4.xsd', 33, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_2()

