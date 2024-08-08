#
# 3MF Volumetric & Implicit Extensions

## Specification & Reference Guide



| **Version** | 0.8.0 |
| --- | --- |
| **Status** | Draft |

**Note**

## Table of Contents

- [Preface](#preface)
  * [Introduction](#introduction)
  * [About this Specification](#about-this-specification)
  * [Document Conventions](#document-conventions)
  * [Language Notes](#language-notes)
  * [Software Conformance](#software-conformance)
- [Part I: Volumetric Extension](#part-i-volumetric-extension)
  * [Chapter 1. Overview of Volumetric Additions](#chapter-1-overview-of-volumetric-additions)
  * [Chapter 2. DataTypes](#chapter-2-datatypes)
  * [Chapter 3. Functions](#chapter-3-functions-and-function-types)
  * [Chapter 4. 3D Image](#chapter-4-3d-image)
  * [Chapter 5. LevelSet](#chapter-5-levelset)
  * [Chapter 6. Volumetric Data](#chapter-6-volumetric-data)
  * [Chapter 7. Notes](#chapter-6-notes)
- [Part II. Implicit Extension](#3mf-volumetric-implicit-extensions)
  * [Chatper 1. Overview of Implicit Additions](#chapter-1-overview-of-implicit-additions)
  * [Chapter 2. Function Implicit](#chapter-2-function-implicit)
  * [Chapter 3. Nodes](#chapter-3-nodes)
  * [Chapter 4. Native Nodes](#chapter-4-native-nodes)
  * [Chapter 5. Implicit Evaluation](#chapter-5-implicit-evaluation)
  * [Chapter 6. Notes](#chapter-6-notes)
- [Part III. Appendices](#part-ii-appendices)
  * [Appendix A. Glossary](#appendix-a-glossary)
  * [Appendix B. 3MF XSD Schema for the Volumetric and Implicit Extensions](#appendix-b-3mf-xsd-schema-for-the-volumetric-extension)
  * [Appendix C. Standard Namespace](#appendix-c-standard-namespace)
  * [Appendix D: Example file](#appendix-d-example-file)
- [References](#references)



# Preface

## Introduction
Volumetric/Implicit Modeling is an efficient approach to encode geometrical shapes and spatial properties and is based on a volumetric description.
Traditional, explicit modeling methodologies are based on surfaces (e.g. NURBS, triangular meshes) that describe the boundaries of an object. This is illustrated in Figure 1-1. a) a NURBS surface delimitates a region of space. Figure 1-1 b) shows a triangular mesh that describes the same surface. In each case, the top part of the described object is being shown transparently to allow viewing the "inside" of the described object.

The implicit modeling approach relies on a mathematical, field-based description of the whole volume of the object. This is illustrated in Figure 1-1 c). Every point in space has a scalar (grey-scale) value. The iso-surface at value 0 describes the surface of the same object as in Figure 1-1 a). A section of this iso-surface is indicated by the blue line.

The true advantage of volumetric modeling shows when properties of an object vary in space gradually, e.g. color or material-distribution and -composition of an object vary in space. E.g. in Figure 1-2 a) the object has a uniform color except for a red stripe at the front-left surface that gradually turns into turquoise. Note that not only the surface, but also the interior volume has a non-uniform color in this region. Figure 1-2 b) shows a distribution of three different materials, indicated by three different colors, red, blue and green.

This is only a brief illustration of the implicit modeling approach to geometric design and more information can be found in [references](#references) \[1\] and \[2\].

_Figure 1-1. Explicit (a) and (b) vs. implicit (c) representation_
![Explicit vs. implicit representation](images/explicit_vs_implicit.png)

_Figure 1-2. Spatially varying properties_
![Volumetric properties](images/spatially_varying_property.png)

## About this Specification

![Volumetric image](images/volumetric_image1.png)

This 3MF volumetric specification is an extension to the core 3MF specification. This document cannot stand alone and only applies as an addendum to the core 3MF specification. Usage of this and any other 3MF extensions follow an a la carte model, defined in the core 3MF specification.

This 3MF implicit specification is an extension to the core 3MF specification and the 3MF volumetric specification. This document cannot stand alone and only applies as an addendum to the core 3MF specification. Usage of this and any other 3MF extensions follow an a la carte model, defined in the core 3MF specification.

Part I, "Volumetric Extension," presents the details of the primarily XML-based 3MF Document format. This section describes the XML markup that defines the composition of 3D documents and the appearance of each model within the document.

Part II, "Implicit Extension," describes the XML markup for describing implicit functions and their evaluation by defining a graph of nodes and their connections.

Part III, "Appendices," contains additional technical details and schemas too extensive to include in the main body of the text as well as convenient reference information.

The information contained in this specification is subject to change. Every effort has been made to ensure its accuracy at the time of publication.

This extension MUST be used only with Core specification version 1.3. or higher.

## Document Conventions

See [the 3MF Core Specification conventions](https://github.com/3MFConsortium/spec_core/blob/1.2.3/3MF%20Core%20Specification.md#document-conventions).

In this extension specification, as an example, the prefix "m" maps to the xml-namespace "http://schemas.microsoft.com/3dmanufacturing/material/2015/02", "v" to "http://schemas.3mf.io/3dmanufacturing/volumetric/2022/01" and "i" to "http://schemas.3mf.io/3dmanufacturing/implicit/2023/12". See Appendix [E.3 Namespaces](#e3-namespaces).

## Document Conventions

See [the standard 3MF Document Conventions documentation](https://github.com/3MFConsortium/spec_resources/blob/master/document_conventions.md).

## Language Notes

See [the standard 3MF Language Notes documentation](https://github.com/3MFConsortium/spec_resources/blob/master/language_notes.md).

## Software Conformance

See [the standard 3MF Software Conformance documentation](https://github.com/3MFConsortium/spec_resources/blob/master/software_conformance.md).


# Part I. Volumetric Extension

## Chapter 1. Overview of Volumetric Additions

_Figure 1-1: Overview of model XML structure of 3MF with volumetric additions_
![Overview of model XML structure of 3MF with volumetric additions](images/overview-of-additions.png)

This document describes new elements, each of which is OPTIONAL for producers. Consumers MUST be able to parse all new elements but only MUST support levelset shape.

There are two central ideas of this extension. The first is to provide a new geoemtry representation as an alternative to a mesh using levelsets. The second is to enrich the geometry notion of 3MF with volumetric elements that can represent spatially varying properties which are quite inefficient to handle with a mesh representation, especially in cases where the variation is continuous in space.

This extension is meant to be an exact specification of geometric, appearance-related, material and in fact arbitrary properties, and consumers MUST interpret it as such. However, the intent is also to enable editors of 3MF files to use the designated data structures for efficient interoperability and post-processing of the geometry and properties described in this extension.

A producer using the level set of the volumetric specification MUST mark the extension as required, as described in the core specification. Producers only using the other volume data elements, in particular color-, composite- and property-elements, MAY mark the extension as REQUIRED, and MAY be marked as RECOMMENDED. Consumers of 3MF files that do not mark the volumetric extension as required are thus assured that the geometric shape of objects in this 3MF file are not altered by the volumetric specification.

# Chapter 2. DataTypes

The volumetric extension of 3MF, defines 4 new datatypes that are used for definition of the outputs of functions for volumetric evaluation. 
They allow to reference the output of nodes in a graph for the implicit extension or define the mapping of the output channels for the sampling of an image3d with functionFromImage3D. The References are of the type ST_NodeOutputIdentifier.

## 2.1 ST_NodeOutputIdentifier
The `ST_NodeOutputIdentifier` is a simple type used to represent an identifier for a node output in the format of "nodename.outputname".

ST_ScalarID, ST_VectorID, ST_MatrixID and ST_ResourceOutputID are derived from ST_NodeOutputIdentifier.

### Format
The format of `ST_NodeOutputIdentifier` is "nodename.outputname". The identifier must consist of alphanumeric characters and underscores. The dot (.) separates the node name and the output name.

## 2.2 ScalarReference
Element `<scalarref>`

![Scalar XML Structure](images/element_scalarreference.png)
| Name      | Type             | Use      | Default | Annotation                                                                 |
| --------- | ---------------- | -------- | ------- | -------------------------------------------------------------------------- |
| identifier| ST_Identifier    | required |         | Specifies an identifier for this scalar resource.                          |
| displayname| xs:string       | optional |         | The name to be displayed e.g. for annotation
| ref       | ST_ScalarID      | required |         | Reference to the scalar in the form "NodeIdentifier.ScalarIdentifier".  

## 2.3 VectorReference
Element `<vectorref>`

![Vector XML Structure](images/element_vectorreference.png)
| Name      | Type             | Use      | Default | Annotation                                                                 |
| --------- | ---------------- | -------- | ------- | -------------------------------------------------------------------------- |
| identifier| ST_Identifier    | required |         | Specifies an identifier for this vector resource.                          |
| displayname| xs:string       | optional |         | The name to be displayed e.g. for annotation. |
| ref       | ST_VectorID      | required |         | Reference to the scalar in the form "NodeIdentifier.VectorIdentifier".   |

## 2.4 MatrixReference
Element `<matrixref>`

References to functions are only used for the implicit extension.

![Vector XML Structure](images/element_matrixreference.png)
| Name      | Type             | Use      | Default | Annotation                                                                 |
| --------- | ---------------- | -------- | ------- | -------------------------------------------------------------------------- |
| identifier| ST_Identifier    | required |         | Specifies an identifier for this matrix resource.                          |
| displayname| xs:string       | optional |         | The name to be displayed e.g. for annotation
| ref       | ST_MatrixID      | required |         | Reference to the scalar in the form "NodeIdentifier.VectorIdentifier".                              |

## 2.5 ResourceReference
Element `<resourceref>`

References to resources are used for the volumeData element and for the implicit extension to create a function reference.

![Function XML Structure](images/element_resourcereference.png)
| Name      | Type             | Use      | Default | Annotation                                                                 |
| --------- | ---------------- | -------- | ------- | -------------------------------------------------------------------------- |
| identifier| ST_Identifier    | required |         | Specifies an identifier for this function resource.                          |
| displayname| xs:string       | optional |         | The name to be displayed e.g. for annotation
| ref       | ST_ResourceOutputID      | required |         | Reference to the resource output in the form "NodeIdentifier.OutputIdentifier".                              |


# Chapter 3. Functions and Function Types

## 3.1 Functions
Complex Type **CT_Function**

![Function XML Structure](images/CT_Function.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| id | ST\_ResourceID | required | | Specifies an identifier for this function resource. |
| displayname | xs:string | | | Function resource name used for annotations purposes. |

Volumetric data is created with functions that are evaluatable for at given model position. Each `<function>` element is assumed to represent a method which can be evaluated within the model being described. Functions have input arguments and output arguments, each argument MUST be one of the supported datatypes enumerated in Chapter 2.

`<function>` is a container for one of three distinct function types: FunctionFromImage3d, PrivateExtensionFunction, FunctionImplicit. The only function type that MUST be supported for the volumetric extension is FunctionFromImage3D which requires an Image3d resource.

## 3.2 FunctionFromImage3D
Element **\<functionFromImage3d>**

![FunctionFromImage3d XML](images/element_functionformimage3d.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| id | ST\_ResourceID | required | | Specifies an identifier for this function resource. |
| displayname | xs:string | | | Function resource name used for annotations purposes. |
| image3did | ST\_ResourceID | required | | Specifies an identifier for the image3d resource that this function uses during evaluation. |
| valueoffset | xs:double | optional | 0.0 | Specifies a numerical offset for the samples values |
| valuescale | xs:double | optional | 1.0 | Specifies a numerical scaling of the sampled values |
| filter |ST\_Filter | | linear | "linear" or "nearest" neighbor interpolation. |
 tilestyleu | ST\_TileStyle | | wrap | Determines the behavior of the sampler for texture coordinate u outside the [0,1] range. |
| tilestylev | ST\_TileStyle | | wrap | Determines the behavior of the sampler for texture coordinate v outside the [0,1] range. |
| tilestylew | ST\_TileStyle | | wrap | Determines the behavior of the sampler for texture coordinate w outside the [0,1] range. |

Elements of type `<functionfromimage3d>` define a function which can be sampled at any point in space from values on a voxel grid defined in the `<image3d>` element. The function is evaluated by sampling the image3d at the UVW coordinates of the model position. The UVW coordinates are determined by the filter-rule and the tilestyle attributes of the `<functionfromimage3d>`-element.

To simplify parsing, producers MUST define `<image3d>`-elements prior to referencing them via imaged3did in a `<functionfromimage3d>`-element.

**tilestyle-u, -v or -w**:

MUST be one of "wrap", "mirror" or  "clamp". This property determines the behavior of the sampler of this `<functionfromimage3d>` for 3d texture coordinates (u,v,w) outside the [0,1]x[0,1]x[0,1] cell. The different modes have the following interpretation (for s = u, s = v, or s = w):

1. "wrap" assumes periodic texture sampling, see Figure 3-1 a). A texture coordinate s that falls outside the [0,1] interval will be transformed per the following formula:
</br>s’ = s – floor(s)

2. "mirror" means that each time the texture width or height is exceeded, the next repetition of the texture MUST be reflected across a plane perpendicular to the axis in question, see Figure 3-1 b). This behavior follows this formula:
</br>s’ = 1 - abs( s - 2 * floor(s/2) - 1 )

3. "clamp" will restrict the texture coordinate value to the [0,1] range, see Figure 3-1 c). A texture coordinate s that falls outside the [0,1] interval will be transformed according to the following formula:
</br>s’ = min(1, max(0,s))

	_Figure 3-1: Illustration of different tilestyles. a) tilestyle wrap illustrated throughout the second `<imagesheet>`. b) tilestyle mirror illustrated throughout the second `<imagesheet>`. c) tilestyle clamp along the u-direction illustrated throughout the second `<imagesheet>`_
	![Tilestyles](images/tilestyle_all.png)

**filter**:
The filter attribute defines the interpolation method used when a `<functionfromimage3d>` is being sampled. This is illustrated in Figure 3-4.

- If the interpolation method of an element of type `<functionfromimage3d>` is "nearest", sampling it at an arbitrary (u,v,w) returns the floating point value defined by the closest point (u',v',w') to (u,v,w) which transforms back to a voxel center in the 3D image resource. If a coordinate u,v, or w maps exactly at the middle between to voxel centers, sampling (u,v,w) should return the floating point value defined by the voxel center with the lower index value of the two voxel centers in question.

	_Figure 3-3: voxel lookup using filter method "nearest" neighbor: sampling at uvw=(1/8,2/3,0) evaluates the voxel with index-triple (0,0,0) (not (1,0,0)), and sampling at (u,v,w)=(0.5,0.5,0) evaluates the voxel with index-triple (1,1,0) (not (1,2,0))._

	![Voxel lookup using filter method "nearest" neighbor](images/lookup_filter_nearest.png)


- If the interpolation method of an element of type `<functionfromimage3d>` is "linear", sampling it at an arbitrary (u,v,w) returns the floating point defined by trilinearly interpolating between the eight point coordinates defining a box that contains the arbitrary (u,v,w), which transforms back to voxel centers in the 3D image resource.

_Figure 3-4: filter attributes "nearest" (a) and "linear" (b). The greyscale channel ("Y") of the image 3d of Figure 3-1 is reused in this example. The region shown is clipped at w=0.75, v=1/6 and u=2. The grey wireframe box indicates the UVW unit box. The tilesyle is "wrap" in all directions._
![Tilestyle mirror](images/filter.png)

**`offsetvalue` and `scalevalue`**:

The values `V'` sampled from the `<image3d>` are linearly scaled via `offsetvalue` and `scalevalue` giving a sampled value `V'' = V'*scalevalue + offsetvalue`


A `<functionfromimage3d>` is a container for an image3D which is evaluatable. In contrast to implict functions, the inputs and outputs of a functionfromimage3d are fixed and are not defined in the markup.

The ouputs can be referenced by `<volumedata>` elements (e.g. `<color>`) or `<levelset>` using the `channel` attribute. In the implicit namespace a `<functionfromimage3d>` can be referenced by a functionCall-Node in the same way as a implicit function with the listed inputs and outputs.

A `<functionfromimage3d>` has the following input and outputs:

**Inputs:**
| Identifier | Type |	Description |
|------------|-------------|-------------|
| pos        | vector    | UVW coordinates of the point to be evaluated. Points outside the range from (0, 0, 0) to (1 , 1, 1) will be mapped according to the tile style |

The ouput values are in the range from 0 to 1. Please see [Chapter 4.2](#42-imagestack) for more information on the input pixel layouts.

**Outputs:**
| Identifier | Type |	Description |
|------------|-------------|-------------|
| color      | vector    | Vector containing the rgb values (x=red, y=green, z=blue), alpha is ignored |
| red		 | scalar    | Scalar containing the red value |
| green		 | scalar    | Scalar containing the green value |
| blue		 | scalar    | Scalar containing the blue value |
| alpha      | scalar    | Scalar containing the alpha value |

The appearance of color and red, green, blue might seem redundant, but allows to also use the output directly as a vectorial field. 

**Example Usage:**
```xml
 
<v:image3d id="2">
			<v:imagestack rowcount="821" columncount="819" sheetcount="11">
				<v:imagesheet path="/volume/layer_01.png"/>
				...
			</v:imagestack>
		</v:image3d>
<v:functionfromimage3d id="3" displayname="function from image3d" image3dID="2" offset="0" scale="1400" tilestyleu="wrap" tilestylev="clamp" tilestylew="mirror" filter="linear"></v:functionfromimage3d>
...
<mesh>
	<vertices>
		...
	</vertices>
	<triangles>
		...
	</triangles>
	<v:volumedata>
		<v:property name="Temp" transform="0.01 0 0 0 0.01 0 0 0 0.01 0.5 0.5 0.5" functionid="3" channel="red"/>
	</v:volumedata>
</mesh>

```

## 3.3 PrivateExtensionFunction
Element **\<PrivateExtensionFunction>

![PrivateExtensionFunction XML](images/element_privateextensionfunction.png)
| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| id | ST\_ResourceID | required | | Specifies an identifier for this function resource. |
| displayname | xs:string | | | Function resource name used for annotations purposes. |
| xmlns | ST\_namespace | required | | Specifies the namespace of the function. |

PrivateExtensionFunction is an OPTIONAL function type to support. This function can take either a <scalar> or <vector> input and returns either a <scalar> or <vector>. The intent of this function type is to allow users to extend the volumetric specification for custom functionality that is not possible with the existing functions.

## 3.4 ImplicitFunction
Element **\<i:implicitfunction>

![ImplicitFunction XML](images/element_implicitfunction.png)
| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| id | ST\_ResourceID | required | | Specifies an identifier for this function resource. |
| displayname | xs:string | | | Function resource name used for annotations purposes. |
| xmlns | ST\_namespace | required | implict | Specifies the namespace of the function. |

ImplicitFunction is an OPTIONAL function type to support for the Volumetric specification in the  _implicit_ namespace. The function requires an input DataType and an output DataType. 

# Chapter 4. 3D Image

## 4.1 3D Image

Element **\<image3d>**

![Image3D XML structure](images/element_image3d.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| id | ST\_ResourceID | required | | Specifies an identifier for this image3d resource. |
| name | xs:string | | | 3d image resource name used for annotations purposes. |

Volumetric data can be encoded as 3d images that consist of voxels. Each `<image3d>` element is assumed to represent a finite voxel grid from which data can be sampled.

`<image3d>` is a container for different representations of voxeldata. This specification defines only the `<imagestack>`-elements. Later versions of this specification might provide alternative child elements for the `<image3d>` element.

## 4.2 ImageStack

Element **\<imagestack>**

![ImageStack XML structure](images/element_imagestack.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| rowcount | xs:positiveinteger | required || Number of pixel rows in all child `<imagesheet>`-elements. |
| columncount | xs:positiveinteger | required || Number of pixel columns in all child `<imagesheet>`-elements. |
| sheetcount | xs:positiveinteger | required || Number of `<imagesheet>`-elements within this `<imagestack>` element. |

Volumetric images can be embedded inside a 3MF file using groups of PNG images that represent a stack of images.

All `<imagesheet>`-elements within an imagestack MUST have the same number of rows and columns that is specified in the rowcount and columncount-attributes, respectively. rowcount, columncount and sheetcount MUST not exceed 1024^3, each. The total number of voxels MUST be limited by 1024^5. There MUST be exactly sheetcount `<imagesheet>`-elements under `<imagestack>` that are implicitly ordered starting with index 0.

Imagestack objects, and thus all underlying `<imagesheet>` elements, MUST follow one of the input pixel layouts shown in the table below. All imagesheets within an imagestack MUST have the same input pixel layouts, and each channel MUST have the same bit-depth across all imagesheets. Pixel values sampled from a PNG file with a bitdepth of `N` bits will be normalized to 
`pixelvalue / (2^N-1)`, i.e. a fully separated channel is normalized to 1, the minimum sampled value is normalized to 0.

The following table shows the logical interpretation of sampling the "R", "G", "B" or "A"-channel depending on the input pixel layouts. The meaning of symbols is as follows: R – red, G – green, B – blue, A – alpha, Y – greyscale.

| Input pixel layout | | | | | |
| --- | --- | --- | --- | --- | --- |
| RGBA | R | G | B | A |
| RGB | R | G | B | 1 |
| YA | Y | Y | Y | A |
| Y | Y | Y | Y | 1 |

For example, if a function output from `<functionfromimage3d>` in a 3MF-file that maps to the R(ed) channel, but the referenced image is only monochromatic, then the greyscale channel is interpreted as the R color channel. Similarly, color values sampled from a monochromatic image are interpreted as if all "R", "G", "B" color channels share the same greyscale value. If there is no alpha channel present in the image, the highest possible value `1` MUST be used.

The `<imagestack>`-element defines a voxel grid of values (e.g. RGB, grey-Alpha, grey) values distributed in a cuboid ({0,1,...,rowcount-1} x {0,1,...,columncount-1} x {0,1,...,sheetcount-1}). The left-front-bottom corner of this grid corresponds to the (0,0,0)-UVW coordinate when this 3D Image is being sampled, whereas the right-back-top corner corresponds to the (1,1,1) UVW-coordinate. Each `<imagesheet>` corresponds to one PNG-file in the package. Figure 2-1 a) illustrates a voxel grid with `rowcount=3`, `columncount=4` and `sheetcount=2` voxels. Voxel indices are shown as bold black triple, the UVW-coordinate values as red triples.
Figure 2-1 b) illustrates the voxel indices and the UVW-values throughout the first `<imagesheet>`, Figure 2-1 c) illustrates these quantities throughout the second `<imagesheet>`. A voxel index triple `(i,j,k)` corresponds to a voxel with rowindex `i`, columnindex `j` and sheetindex `k`.

__Note__: The columnindex (`j`) relates to the UVW-coordinate `U`, whereas the rowindex `i` relates to the UVW-coordinate `V`. This definition is inline with the
Materials and Properties specification https://github.com/3MFConsortium/spec_materials/blob/1.2.1/3MF%20Materials%20Extension.md#chapter-6-texture-2d.

The sampling rules for UVW values are determined by the filter-rule, and the behavior for UVW-values outside the unit-cube are determined by the tilestyle attributes [of the `<functionfromimage3d>`](#32-functionfromimage3d).

_Figure 2-1: Voxel indixes and UVW-texture space of a sample voxel grid: a) shows a voxel grid of 3x4x2 voxels. b) shows a section view of the bottom voxels, c) shows a section view of the top voxels. The orange voxel at the right, front and bottom of a) has rowindex=2, columnindex=3 and sheetindex=0. d) shows the voxelcenters of this configuration._
![Voxel indices and UVW-texture space of a sample voxel grid](images/image3dcoordinates.png)

## 4.1.1 File Formats
PNG images can provide acceptable compression and bit-depth for the boundary-function, color information, material mixing ratios or arbitrary property information.

The following describes recommendations for the channel bit depth of PNG images used in this specification and is based on the nomenclature in the specification of the Portable Network Graphics (PNG, https://www.w3.org/TR/PNG) format.

- Color information, material mixing ratios and arbitrary properties can be deduced from PNG images with arbitrary channel depth. It is RECOMMENDED to store color into RGB-channels within a PNG.

- It is RECOMMENDED to store image information that will be used as levelset-function to represent a boundary in PNGs with one channel only. A typical approach to store this levelset information is to encode the signed distance field of the boundary of the object in this channel, or to limit the encoding to a narrow region around the boundary of the object. A different option is to deduce the levelset-function from a channel with binary values, i.e. from images of image type "greyscale" with bit-depth of 1 or an indexed-color with bit depths of 1, but with a very high spatial resolution.

	_Figure 2-2: 2D-slice through the levelset representation of a sphere of radius 5 illustrated as red circle. a) the greyscale values of the image represent the signed distance function in a box around the sphere. Values range from -10 to 10. b) High resolution image of the slice. White indicates a point that is inside the sphere, black outside the sphere. c) Image encoding the signed distance in a narrow band of thickness 2 around the boundary of the sphere. Values outside this band only indicate whether the point is inside or outside the sphere, as in b)._
	![Leveset representation of a sphere ](images/illustration_boundary.png)


- Producers SHOULD store information for which they require high resolution in image channels with bit depth of 16. Most professional image editing tools and standard implementations of the PNG format support channels with 16 bit.


## 4.2.2 OPC package layout
__Note__: Introductory information about the Open Packaging Conventions (OPC) can be found in the 3MF Core Specification (see https://github.com/3MFConsortium/spec_core/blob/1.3.0/3MF%20Core%20Specification.md#11-package).

It is RECOMMENDED that producers of 3MF Documents with the Volumetric Extension specification use the following part naming convention:

Paths of `<imagesheet>` SHOULD consist of four segments. "/3D/volumetric/" as the first two segments, the name of a `<image3d>`-element that references this `<imagesheet>` as third segment (for example "/3D/volumetric/mixingratios/", and the name of the imagesheet as last segment (for example "sheet0001.png"). Each part in the 3MF package that is referred to by the path of an `<imagesheet>` MUST be associated with the 3D Model part via the 3D Texture relationship.

This implies that all parts for `<imagesheet>` in an imagestack SHOULD be located in the same OPC folder.

_Figure 2-3: OPC package layout_
![OPC package layout](images/OPC_overview.png)

## 4.2.3 3D Image Sheet

Element **\<imagesheet>**

![imagesheet XML structure](images/element_imagesheet.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| path | ST\_UriReference | required | | Specifies the OPC part name (i.e. path) of the image data file |

Each `<imagesheet>` element has one required attribute. The path property determines the part name (i.e. path) of the 2D image data (see chapter 6 of the Materials & Properties Extension specification for more information).

__Note__:
Other file formats like OpenVDB, OpenEXR, or VTK offer similar functionality as a stack of PNGs and are more efficient at doing so. However, their use in a manufacturing environment is hard as these formats are conceptually more complex and harder to implement. Therefore, this specification relies on the human readable and conceptually simpler stack of PNGs. Later versions of this extension, or private extension of the 3MF format MAY use different 3D image formats to encode a volumetric data as different child elements of `<image3d>` and benefit from their advanced features. The remainder of this specification deals with the mapping of volumetric data onto mesh-objects in a 3MF file and giving this volumetric data a meaning for additive manufacturing processes. Adding a different data format for a voxel grid as child under `<image3d>` would not affect the remaining parts of this specification.

# Chapter 5 LevelSet
### 5.1.1 LevelSet element

A powerful application of Volumetric and Implicit modeling is the ability to define the shape of an object from volumetric information. Therefore we are introducing the concept of a **\<levelset>** element which can be used to define the boundary of a shape using a levelset function. This is analogous to how a mesh defines the boundary between the inside and outside of the shape. In this case the mesh surface represents the surface of the levelset value equal to zero.

The child-element of the `<levelset>`-element references a functionID that must have a scalar output. This 'shape' represents the levelset function that MUST be evaluated to determine the actual shape of the object.

Since fields can be evaluated in an unbounded way, a closed mesh is required to enclose any levelset element to make the evaluation space bounded. For example a simple box that represents the bounding box of the geometry encoded in the `<meshid>`-element. There are cases where a producer would want to specify a bounding box for evaluation. In that case one can set the the `<meshbboxonly>`-element to true and the `<levelset>`-element must be evaluated within the extents of the mesh referenced by the `<meshid>`-element.

Element **\<levelset>**

![levelset XML structure](images/element_levelset.png)

| Name           | Type         | Use      | Default | Annotation                                                           |
| -------------- | ------------ | -------- | ------- | -------------------------------------------------------------------- |
| functionid     | ST_ResourceID| required |         | ResourceID of the `<function>` that provides the boundary as a level set. |
| channel      | xs:QName  | required |         | Name of the output of the function to be used for the levelset. The output must be a scalar |
| transform      | ST_Matrix3D  |          | Identity | Transformation of the object coordinate system into the `<function>` coordinate system. |
| minfeaturesize | ST_Number    |          | 0.0     | Specifies the minimum size of features to be considered in the boundary. |
| meshid     | ST_ResourceID| required |         | ResourceID of the `<mesh>` that is used to define the evaluation domain of the level set.|
| meshbboxonly   | xs:boolean   |          | false   | Indicates whether to consider only the bounding box of the mesh for the level set. |
| fallbackvalue	 | ST_Number	|		   | 0.0	 | Specifies the value to be used for this data element if the output of the referenced function is undefined |
| volumeid     | ST_ResourceID |		   |         | ResourceID of a `<volumedata>`-Resource to apply on the object |


The  `<levelset>`-element is used to describe the interior and exterior of an object via a levelset function.

If meshbboxonly is set to true, the boundary is only intersected with the bounding box of the mesh. This allows the consumer to evaluate the boundary without computing the intersection with the mesh, otherwise the boundary is intersected with the mesh.

To simplify parsing, producers MUST define a `<function>`>-element prior to referencing it via the functionid-attribute in a `<levelset>`-element.

**functionid**:

ResourceID of the `<function>` that provides the boundary as a levelset. The function MUST have an input of type vector with the name "pos" and an output of type scalar that matches the name given as the channel attribute of the `<levelset>` element.

**channel**:
Defines which function output channel is used as the levelset function. The channel MUST be of type scalar.

**transform**:

The transformation of the object coordinate system into the scalar field coordinate system.
If the boundary-property of the enclosing mesh is being sampled at position `(x,y,z)` in the mesh's local object coordinate system, the referenced scalar field must be sampled at position `(x',y',z') = T*(x,y,z)`.
See Figure 6-1 for an illustration of this transform in the sampling process.


**minfeaturesize**:

The minimum size of features to be considered in the boundary. This is used as a hint for the consumer to determine the resolution of the boundary. If the consumer is not able to resolve features of this size, it SHOULD raise a warning.

**meshbboxonly**:

If this attribute is set to "true", the boundary is only intersected with the bounding box of the mesh. This allows the consumer to evaluate the boundary without computing the intersection with the mesh.

**fallbackvalue**:

Any undefined result MUST be evaluated as the value provided.

**VolumeDetermination**

_Figure 5-1: a) LevelSet A with a Mesh clipping surface. b) Mesh object B (rectangle) with `<volumedata>` child element Y. The mesh objects are defined in the order A-B. c) shows the volume defined by the overlapped mesh objects. d) shows `<volumedata>` child element X in object A, and `<volumedata>` child element Y in object B. The table lays out how these `<volumedata>` child elements are sampled at positions p1 to p4._
![Illustration of overlapping meshes with `<volumedata>` child elements](images/overlap_properties.png)


# Chapter 6. Volumetric Data

## 6.1. Volumetric Data extension to Resources
 
Element **\<Resource>**

![mesh XML structure](images/element_mesh.png)

The volumetric data `<volumedata>` element is a new OPTIONAL element which extends is a type of resource to be used by a Shape (i.e. the `<shape>` element).


## 6.2. Volumetric Data

Element **\<volumedata>**

![volumedata XML structure](images/element_volumedata.png)

The `<volumedata>` defines the volumetric properties in the interior of a `<shape>` element.

The child-element of the `<volumedata>` element reference a function, that has to match the signature requirements of the child element. 
Volumedata MUST only be referenced by an object type "mesh" or "levelset" unless explicitly allowed by shapes defined in other extensions. This ensures that the `<volumedata>` applies to a volume.
Moreover, the volumedata-element MUST not be used in a mesh that is referenced as "originalmesh" by any other mesh. This excludes the possibility to implicitly mirror volumedata, which makes it easier to consume files with this extension.

The `<volumedata>` element can contain up to one `<composite>` child element, up to one `<color>` element, and up to 2^31-1 of `<property>` elements.

The child elements modify the enclosing `<shape>` by specifying color, material composition and other arbitrary properties of the `<shape>` object.

To rationalize how this specification modifies the definition of geometry within a 3MF model, the concept of a "clipping surface" of a mesh with a `<volumedata>` element is introduced.
The clipping surface is defined by the surface of the enclosing `<shape>` element. This implicitly takes into account any geometry defined by e.g. the beamlattices specification.

This clipping surface trims any volumetric data defined therein. Any data outside the clipping surface MUST be ignored. The geometry that should be printed is defined by the interior of the clipping surface.


__Note__
Volumetric content is always clipped to the clipping surface of the shape that embeds it.
If a property (color, composite or properties) defined at the surface of an object conflicts with the property within the object defined by this extension, the surface property has precedence in the following sense:
The consumer MUST define a surface layer with a thickness as small as possible to achieve the surface property on the outside of the object. Outside of this thin surface region, the volumetric property MUST be applied everywhere within the object.

__Note__
Defining conflicting surface- and volumetric properties can be very powerful, e.g. if one wants to add a high resolution surface texture over a lower resolution volumetric color. However, producers MUST be aware that the thickness of this surface layer can vary between consumers depending on the manufacturing technology they employ.

The properties at surface regions that are not explicitly specified are instead given by the volumetric properties.

Conflicting properties must be handled as follows:
1. Producers MUST not define colors, materials or properties via child elements of the `<volumedata>` element that are impossible on physical grounds (e.g. non-conducting copper).
2. Consumers that read files with properties that cannot be realized due to limitations specific to them (e.g. a specific manufacturing device that does not support a material in a specific color), SHOULD raise a warning, but MAY handle this in any appropriate way for them. If there is an established process between Producer and Consumer, resolution of such conflicts SHOULD be performed e.g. via negotiation through printer capabilities and a print ticket.

__Note__: In the case where objects with different `<volumedata>` child elements overlap, only the `<volumedata>` child elements from last object can be used.
This makes sure that `<volumedata>` child elements of an overlapped object do not determine the value of any `<volumedata>` child elements of an overlapping object. Figure 5-1 illustrates this behavior.

### 6.2.1 Color element

Element **\<color>**

![color XML structure](images/element_color.png)

| Name            | Type           | Use      | Default | Annotation                                                |
| --------------- | -------------- | -------- | ------- | --------------------------------------------------------- |
|| functionid      | ST_ResourceID  | required |         | Model Resource Id of the function providing the color                                                          |
| transform       | ST_Matrix3D    |          |         | Transformation of the object coordinate system into the `<function>` coordinate system. |
| channel         | xs:QName       | required |         | Name of the function ouput to be used as color. The output must be of type vector |
| minfeaturesize  | ST_Number      |          |  0.0       | Hint for the minimum size of features. |
| fallbackvalue	 | ST_Number	|		   | 0.0	 | Specifies the value to be used for this data element if the output of the referenced function is undefined |

To simplify parsing, producers MUST define a `<vector3dfield>`-element prior to referencing it via the vector3dfieldid in a `<color>`-element.

The `<color>` element is used to define the color of the object.
The color MUST be interpreted in linearized sRGB color space as defined in the Materials and Properties specification https://github.com/3MFConsortium/spec_materials/blob/1.2.1/3MF%20Materials%20Extension.md#12-srgb-and-linear-color-values.

The vector components `x`, `y` and `z` of the 3D vector field are interpreted as the "R", "G" and "B" channels of the color of the enclosing meshobject, respectively. If either channel evaluates to a value \<0 or \>1 it has to be truncated at 0 or 1, respectively.

This specification does not capture well the properties for semi-transparent, diffusive materials. This specification is useful for defining parts with non transparent, opaque materials, e.g. for indicating wear and tear, sectioning the models and printing with non transparent materials.

**transform**:

The transformation of the object coordinate system into the coordinate system of the function (e.g. noramlized coordinates for functionFromImage3D).
If this `<color>`>-element is being sampled at position `(x,y,z)` in the mesh's local object coordinate system, the 3D vector field must be sampled at position `(x',y',z') = T*(x,y,z)`.

**channel**

Name of the function ouput to be used as color. The output must be of type vector.

**minfeaturesize**:

The minimum size of features to be considered in the color. This is used as a hint for the consumer to determine the resolution of the color estimation. It might also be used to determine the level of super sampling requiered, if the printer cannot reproduce the resolution. If the consumer is not able to resolve features of this size, it SHOULD raise a warning.

**fallbackvalue**:

Any undefined result MUST be evaluated as the value. The fallback value is specified as a scalar and MUST be applied across the result vector element-wise.

## 6.2.2 Composite element

Element **\<composite>**

![composite XML structure](images/element_composite.png)

| Name   | Type | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| basematerialid | ST\_ResourceID | required | | ResourceID of the `<basematerials>` element that holds the `<base>`-elements referenced in the child `<materialmapping>`-elements. |

The `<composite>` element describes a mixing ratio of printer materials at each position in space. The CONSUMER can determine the halftoning, mixing or dithering strategy that can be used to achieve these mixtures.

This element MUST contain at least one `<materialmapping>` element, which will encode the relative contribution of a specific basematerial to the material mix.

The number of `<base>`-elements in the `<basematerials>` element referenced by a `<composite>` element MUST equal the number of `<materialmapping>`-elements in the `<composite>` element. To simplify parsing, producers MUST define the referenced `<basematerials>`-element prior to referencing it via the basematerialid in a `<composite>`-element.

Producers MUST NOT create files where the sum of all values in its child `<materialmapping>`-elements is smaller than `10^-5`. If the total is smaller than this threshold, the mixing ratio is up to the consumer.

- If there are `N` materials, then the mixing ration of material `i` at point `X` is given by:
   ```
   value of channel i / sum(value of all N mixing contributions at point X)
   ```

The order of the <materialmapping>-elements defines an implicit 0-based index. This index corresponds to the index defined by the `<base>`- elements in the `<basematerials>`-element of the core specification.

## 6.2.3 Material mapping element

Element **\<materialmapping>**

![materialmapping XML structure](images/element_materialmapping.png)

| Name           | Type          | Use      | Default | Annotation                                                |
| -------------- | ------------- | -------- | ------- | --------------------------------------------------------- |
| functionid  | ST_ResourceID | required |         | ResourceID of the `<function>` providing the mixing contribution value for a material in the `<basematerial>`-element. |
| transform      | ST_Matrix3D   |          |         | Transformation of the object coordinate system into the `<function>` coordinate system |
| channel        | xs:QName      | required |         | Name of the function output to be used for the mixing contribution. The output must be a scalar. |
| minfeaturesize | ST_Number     |          | 0       | Hint for the minimum size of features. |
| fallbackvalue	 | ST_Number	|		   | 0.0	 | Specifies the value to be used for this data element if the output of the referenced function is undefined |

The `<materialmapping>` element defines the relative contribution of a specific material to the mixing of materials in it's parent `<composite>`-element.

To simplify parsing, producers MUST define the referenced `<function>`-element prior to referencing it via the functionid in a `<materialmapping>`-element.

**transform**:

The transformation of the object coordinate system into the scalar field coordinate system.
If any channel of a `<materialmapping>` is being sampled at position `(x,y,z)` in the mesh's local object coordinate system, the referenced scalar field must be sampled at position `(x',y',z') = T*(x,y,z)`.

**channel**:

Name of the function output to be used for the mixing contribution. The output must be a scalar. The value is clamped to the range [0,1].

**minfeaturesize**:

The minimum size of features to be considered in the mixing contribution. This is used as a hint for the consumer to determine the resolution of the mixing contribution. If the consumer is not able to resolve features of this size, it SHOULD raise a warning.

**fallbackvalue**:

If this attribute is set, any undefined result MUST be evaluated as the value.

If the sampled value of a `<function>` is `<0` it must be evaluated as "0".

### 6.2.4 Property element

Element **\<property>**

![property XML structure](images/element_property.png)

| Name   | Type   | Use | Default | Annotation |
| --- | --- | --- | --- | --- |
| functionid | ST\_ResourceID | required | | ResourceID of the `<function>` that provides the value of this property |
| transform | ST\_Matrix3D | | | Transformation of the object coordinate system into the `<function>` coordinate system |
| channel | xs:QName | required |  | Name of the function output to be used for the property. |
| name | xs:QName | required | | Contains either the name of the property, defined in a 3MF extension specification, or the name of a vendor-defined property. Either MUST be prefixed with a valid XML namespace name declared on the `<model>` element. |
| required | xs:boolean | | false | Indicator whether this property is required to process this 3MF document instance. |
| fallbackvalue	 | ST_Number	|		   | 0.0	 | Specifies the value to be used for this data element if the output of the referenced function is undefined |

The `<property>` element allows to assign any point in space a scalar or vectorial value of a freely definable property. This can be used to assign, e.g. opacity, conductivity, or translucency.

To simplify parsing, producers MUST define the referenced `<function>`-element prior to referencing it via the functionid in a `<property>`-element.

**transform**:

The transformation of the object coordinate system into the `<function>` coordinate system.
If a `<property>`-element is being sampled at position `(x,y,z)` in the mesh's local object coordinate system, the referenced `<function>` must be sampled at position `(x',y',z') = T*(x,y,z)`.

**channel**:

Name of the function output to be used for the property. Note that the type of the output determines the type of the property.

This specification does not provide qualified names for such properties as part of the standard volumetric namespace.
A later extension of the 3MF format might define such qualified names as part of a different extension specification or a later version of the volumetric extension specification. Producers that want to specify such properties now, SHOULD define a qualified name that can e.g. be called "http://www.vendorwwebsite.com/3mf/vendor13mfextension/2021/05".
The specifications of private namespaces (that are not ratified by the 3MF Consortium) MUST be negotiated between producer and consumer of a 3MF file.

The names of `<property>`-elements MUST be unique within a `<volumedata>`. This name MUST be prefixed with a valid XML namespace name declared on the <model> element.
The interpretation of the value MUST be defined by the owner of the namespace. 
	
__Note__:
The producer of a 3MF file is responsible for assembling the values in the `<property>` (and the referenced `<function>` such that sampling it in the print-bed coordinate system as a e.g. physical property, is sensible. This requirement is particularly important if the accumulated transformation `T0` between print-bed coordinates and local object coordinates is not a rigid body transformation.
(The transformation `T0` of the print-bed coordinate system into the object coordinate system is given by the `transform`-attributes on the `item` and `component`-elements in the path that leads to this object in the `build`-hierarchy of the 3MF Core Specification (see https://github.com/3MFConsortium/spec_core/blob/1.3.0/3MF%20Core%20Specification.md#3431-item-element and https://github.com/3MFConsortium/spec_core/blob/1.3.0/3MF%20Core%20Specification.md#421-component, and Figure 6.2 in this document).

If the interpretation of a property might result in a conflict with the standard volumedata-elements (boundary, color, composite) the namespace-owner MUST specify a resolution to the conflict. A producer MUST NOT create files with properties that conflict with each other.

If a physical unit is necessary, the namespace owner MUST define a unique and unambiguous physical unit system for the namespace. The unit system SHOULD be metric.

If a `<property>` is marked as `required`, and a consumer does not support it, it MUST warn the user or the appropriate upstream processes that it cannot process all contents in this 3MF document instance.
Producers of 3MF files MUST mark all volumetric `<property>`-elements required to represent the design intent of a model as `required`.

# Chapter 7. Notes

## 7.1. Evaluation Graph

The elements in this specification form an acyclic directed graph when evaluating the value of any volumedata-subelement.

It is RECOMMENDED that calculations during evaluation of the graph are performed in at least single-precision floating-point arithmethic, according to IEEE 754.

## 7.2. Evaluation Process

Equipped with the language elements of this specification, one can recapitulate the core concepts with an overview of the sampling process.

Figure 7-1 illustrates the 3MF elements, the different coordinate systems and transforms between them when a `<volumedata>` element (in this case `<color>`) is sampled in the object coordinate space.

Figure 7-1 a) The object's color is sampled at position (+) in the print-bed coordinate system. The clipping surface is hinted at with a wireframe. The transformation `T0` of the print-bed coordinate system into the object coordinate system is given by the `transform`-attributes on the `item` and `component`-elements in the path that leads to this object in the `build`-hierarchy of the 3MF Core Specification (see https://github.com/3MFConsortium/spec_core/blob/1.3.0/3MF%20Core%20Specification.md#3431-item-element and https://github.com/3MFConsortium/spec_core/blob/1.3.0/3MF%20Core%20Specification.md#421-component).

Figure 7-1 b) shows the `<functionfromimage3d>` underlying the color of the object. The sampling point is represented in the coordinate system of the `<functionfromimage3d>`. The transformation `T1` from object coordinate space to `<functionfromimage3d>` coordinate system is given by the `transform`-element in the `<color>`-element. The original clipping surface from a) is only shown for illustration porpuses. It does not exist in the `<functionfromimage3d>` context.
The color value sampled in this illustration directly originates from a `<functionfromimage3d>` element.

Figure 7-1 c) Shows the `<functionfromimage3d>` again. The unit box of the UVW coordinate system is shown as a wireframe. The transformation `T2` between `<functionfromimage3d>` coordinate system and UVW space is given according to the `transform`-attribute of the `<functionfromimage3d>` element.

Figure 7-1 d) Shows the UVW coordinate space of the `<image3d>`-element and where the sampling point (+) is evaluated, and the UVW-locations to which the voxel centers of the underlying `<imagestack>`-element map.

Figure 7-1 e) illustrates where the sampling point (+) ends up in the voxel index space of the `<imagestack>`. The mapping of UVW to voxel indices in the `<imagestack>`-element is described in [Chapter 2. 3D Image](#chapter-2-3d-image).

_Figure 7-1: Illustration of the different coordinate systems and 3MF elements in the sampling process. a) the object to be sampled at position (+). b) A view into the `<functionfromimage3d>`. The original clipping surface from a) is only shown for illustration porpuses. c) Shows the `<functionfromimage3d>` again. The unit box of the UVW coordinate system is shown as a wireframe. d) The UVW coordinate space and the UVW-locations to which the voxel-centers map. e) The sampling point (+) in the voxel index space._
![Illustration of different coordinate systems in the sampling process](images/fig_coordinatesystems.png)

## 7.3. Limitations

This specification is limited in scope. Three noteworthy limitations are:

1. One cannot overlay a function over a meshless (composite) object, one has to duplicate the volume data elements at the object leaves.


2. The fields in this definition are limited to be scalar- (or 1D-vector-) valued and 3D-vector valued. Vectors of other dimensionality must be assembled by the producer / consumer using multiple scalar / 3D-vector fields.

3. It is not possible to assemble a field object that represents the RGB and alpha-channels from images. However one may assamble and blend data from RGBA-images explicitely by extracting the alpha channel into a scalar field and by using the alpha scalar field as a composition mask of two RGB 3d vector fields.

# Part II. Implicit Extension

The implicit namespace extension enriches the volumetric extension by facilitating the use of closed form functions. These provide an alternative to `<functionfromimage3d>` for generating volumetric data.

The functions are members of volumetric data that define a field with arbitrary precision. These functions can be integrated with the existing children of volumedata (materialMapping, property,boundary, color), where they are defined at every point within the mesh or its bounding box. These functions are created via a connected node set. They link inputs and outputs, and allow interaction with other resources.

## Chapter 1. Overview of Implicit Additions
_Figure 1-1: Overview of model XML structure of 3MF with implicit additions_
![Overview of model XML structure of 3MF with volumetric additions](images/fig_overview_implicit.png) Implicit adds FunctionImplicit and Native nodes. Optionally PrivateExtensionFunction can be defined.

## Chapter 2. Function Implicit

The _implicit_ namespace enhances the _volumetric extension_ by providing a way for the definition of closed form functions that can be utilized for generating volumetric data as an alternative to FunctionFromImage3D<functionfromimage3d>. These functions can be nested and can have an arbitrary number of inputs and outputs.

When used as input for `<levelset>`, the functions are evaluated at each point within the mesh or its bounding box. These functions are constructed through a graph-connected node set that is connected to both the function's inputs and outputs. Some of node types allow the usage of other resources, like computing the signed distance to mesh. Also a functionFromImage3D can be called from inside of a function.

Consider an example:
![implicit function of a sphere](images/sphere_graph.png)

```xml
     
    <i:function id="5" displayname="sphere">
        <i:in>
            <i:vector identifier="pos" displayname="pos"></i:vector>
            <i:scalar identifier="radius" displayname="radius"></i:scalar>
        </i:in>
        <i:length identifier="Length_3" displayname="Length_3" tag="">
            <i:in>
                <i:vectorref identifier="A" displayname="A" ref="inputs.pos"></i:vectorref>
            </i:in>
            <i:out>
                <i:scalar identifier="result" displayname="result"></i:scalar>
            </i:out>
        </i:length>
        <i:subtraction identifier="Subtraction_4" displayname="Subtraction_4" tag="">
            <i:in>
                <i:scalarref identifier="A" displayname="A" ref="Length_3.result"></i:scalarref>
                <i:scalarref identifier="B" displayname="B" ref="inputs.radius"></i:scalarref>
            </i:in>
            <i:out>
                <i:scalar identifier="result" displayname="result"></i:scalar>
            </i:out>
        </i:subtraction>
        <i:out>
            <i:scalarref identifier="shape" displayname="shape" ref="Subtraction_4.result"></i:scalarref>
        </i:out>
    </i:function>

```
In this example, the _function_ representing a sphere takes two inputs, a vector 'pos' and a scalar value 'radius'.

Links are defined by back-referencing the output of one node to the input of another node.

The `<i:length>` node computes the length of the input vector 'pos'. The connection to the input vector 'pos' is established through the `<i:vectorref>` element. References have the format [nodename].[outputname]. In the case of funcion arguments the nodename is the resesrved name 'inputs'.

The 'subtraction' node computes the difference between the length of the input vector 'pos' and the scalar value 'radius'. The connection to the length output is established through the `<i:scalarref>` element.

The `<i:out>` element defines the output of the function. The connection to the subtraction output is established through the `<i:scalarref>` element.

It showcases the flexibility of defining various mathematical operations like length computation and subtraction through nested nodes within the function. The result of these computations can be accessed through the `<i:out>` member.


Furthermore, a function can include basic mathematical operations like additions, subtractions, and multiplications to cosines, logarithms or clamping. The operations can use different types like scalars, vectors, and matrices.

This flexible architecture allows the user to define almost any mathematical function with an arbitrary number of inputs and outputs, allowing extensive customization for generating volumetric data.

## Chapter 3. Nodes

A node has an unique identifier and an abritary displayname. A node must not have the identifier "inputs" or "outputs". Identifiers are restricted to alpha-numerical characters.

## Chapter 4. Native Nodes

Overview of native nodes

| Node Type                 | Description                                |
|---------------------------|--------------------------------------------|
| [addition](#addition)     | addition of two values                     |
| [subtraction](#subtraction)    | subtraction operation                      |
| [multiplication](#multiplication) | multiplication operation                   |
| [division](#division)       | division operation                         |
| [constant](#constant)       | constant scalar value                      |
| [constvec](#constvec)       | constant vector                            |
| [constmat](#constmat)       | constant matrix                            |
| [composevector](#composevector) | vector composition operation               |
| [vectorfromscalar](#vectorfromscalar) | vector from scalar operation   |
| [decomposevector](#decomposevector) | vector decomposition operation             |
| [composematrix](#composematrix) | matrix composition operation               |
| [matrixfromcolumns](#matrixfromcolumns) | matrix composition from column vectors |
| [matrixfromrows](#matrixfromrows)       | matrix composition from row vectors    |
| [dot](#dot)                | dot product operation                      |
| [cross](#cross)            | cross product operation                    |
| [matvecmultiplication](#matvecmultiplication) | matrix-vector multiplication operation |
| [transpose](#transpose)        | matrix transpose operation                 |
| [inverse](#inverse)          | matrix inverse operation                   |
| [sin](#sin)                | sine function operation                    |
| [cos](#cos)                | cosine function operation                  |
| [tan](#tan)                | tangent function operation                 |
| [arcsin](#arcsin)          | arcsine function operation                 |
| [arccos](#arccos)          | arccosine function operation               |
| [arctan](#arctan)          | arctangent function operation              |
| [arctan2](#arctan2)        | two-argument arctangent function operation |
| [min](#min)                | minimum value operation                    |
| [max](#max)                | maximum value operation                    |
| [abs](#abs)                | absolute value operation                   |
| [fmod](#fmod)              | Remainder of floating point division       |
| [mod](#mod)                | Modulo operation           				  |
| [pow](#pow)                | power function operation                   |
| [sqrt](#sqrt)              | square root function operation             |
| [exp](#exp)                | exponential function operation             |
| [log](#log)                | natural logarithm function operation        |
| [log2](#log2)              | base 2 logarithm function operation         |
| [log10](#log10)            | base 10 logarithm function operation        |
| [select](#select)          | selection operation                        |
| [clamp](#clamp)            | clamping operation                         |
| [cosh](#cosh)              | hyperbolic cosine function operation        |
| [sinh](#sinh)              | hyperbolic sine function operation          |
| [tanh](#tanh)              | hyperbolic tangent function operation       |
| [round](#round)            | rounding operation                         |
| [ceil](#ceil)              | ceiling operation                          |
| [floor](#floor)            | floor operation                            |
| [sign](#sign)              | signum operation                           |
| [fract](#fract)            | fractional part extraction operation        |
| [functioncall](#functioncall) | function call operation                  |
| [mesh](#mesh)              | signed distance to mesh operation           |
| [unsignedmesh](#unsignedmesh) | unsigned distance to mesh operation     |
| [length](#length)          | length operation                           |
| [constresourceid](#constresourceid)  | constant resource ID                       |


## addition

**Description:**
Performs an addtion of the inputs "A" and "B" and writes the result to the output "result". 

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | First summand                |
| B      | Second summand               |


**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result      | Sum of A and B                |

The operation can be used for the following types of inputs and outputs:

| A   | B   | result   | comment   |
|-----|-----|----------|------------|
| scalar   | scalar   | scalar   |  |
| vector   | vector   | vector   | vector is added componentwise |
| matrix   | matrix   | matrix   | matrix elements are added componentwise |


**Example Usage:**

```xml

<i:addition identifier="addition1" displayname="Addition 1">
    <i:in>
        <i:scalarref identifier="A" ref="constant1.c1"/>
        <i:scalarref identifier="B" ref="inputs.radius"/>
    </i:in>
    <i:out>
        <i:scalar identifier="result"/>
    </i:out>
</i:addition>

```



## constant

**Description:** Node for a constant scalar value. The output must have the identifier "value".

Example:
```xml

<i:constant identifier="constant1" displayname="Constant 1" value="1.0">
    <i:out>
        <i:scalar identifier="value"/>
    </i:out>
</i:constant>

```

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| None         |                                             |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| value        | Constant scalar value                       |


## constvec

**Description:** Node for a constant vector value. The output must have the identifier "vector".

**Inputs:**

None

**Outputs:**

| Identifier | Description |
|------------|-------------|
| vector     | Constant vector value |

**Attributes:**

| Attribute | Type    | Required | Description                  |
|-----------|---------|----------|------------------------------|
| x         | double  | yes      | X-component of the vector     |
| y         | double  | yes      | Y-component of the vector     |
| z         | double  | yes      | Z-component of the vector     |

**Example Usage:**

```xml

<i:constvec identifier="constant1" displayname="Constant 1" x="1.0" y="2.0" z="3.0">
    <i:out>
        <i:vector identifier="vector"/>
    </i:out>
</i:constvec>

```

## constmat

**Description:** Node for a constant 4x4 matrix value. The output must have the identifier "matrix".

**Inputs:**

None

**Outputs:**

| Identifier | Description            |
|------------|------------------------|
| matrix     | Constant 4x4 matrix    |

**Attributes:**

| Attribute | Type          | Required | Description                            |
|-----------|---------------|----------|----------------------------------------|
| matrix    | ST_Matrix4x4 | yes      | The constant 4x4 matrix representation |

**Example Usage:**

```xml

<i:constmat identifier="constant1" displayname="identity" 
    matrix="1.0 0.0 0.0 0.0
            0.0 1.0 0.0 0.0
            0.0 0.0 1.0 0.0 
            0.0 0.0 0.0 1.0">
    <i:out>
        <i:matrix identifier="matrix"/>
    </i:out>
</i:constmat>

```

# constresourceid

**Description:** Defines a model resource id as a constant value.

**Inputs:**

None

**Outputs:**

| Identifier | Description            |
|------------|------------------------|
| value      | Resource ID            |

**Attributes:**

| Attribute | Type               | Required | Description                         |
|-----------|--------------------|----------|-------------------------------------|
| value     | ST_ResourceID     | yes      | The model resource id|

**Example Usage:**

```xml

<i:constresourceid identifier="resourceid1" displayname="Resource Id 1" value="1">
    <i:out>
        <i:resourceid identifier="value"/>
    </i:out>
</i:constresourceid>

```

## composevector

**Description:** Node for composing a vector from 3 scalar values. The inputs must have the identifiers x, y and z.

**Inputs:**

| Identifier | Description            | Type      |
|------------|------------------------|-----------|
| x          | X-coordinate           | scalar    |
| y          | Y-coordinate           | scalar    |
| z          | Z-coordinate           | scalar    |

**Outputs:**

| Identifier | Description            | Type     |
|------------|------------------------|----------|
| result     | Composed vector (x,y,z)       | vector   |

**Example Usage:**

```xml

<i:composevector>
    <i:in>
        <i:scalarref identifier="x" ref="inputs.x"/>
        <i:scalarref identifier="y" ref="inputs.y"/>
        <i:scalarref identifier="z" ref="inputs.z"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:composevector>

```

## vectorfromscalar

**Description:** Node for creating a vector from a single scalar value. The input must have the identifier "A".

**Inputs:**

| Identifier | Description            | Type      |
|------------|------------------------|-----------|
| A          | A -> X, Y, Z           | scalar    |

**Outputs:**

| Identifier | Description            | Type     |
|------------|------------------------|----------|
| result     | vector (A, A, A)        | vector   |

**Example Usage:**

```xml

<i:vectorfromscalar>
    <i:in>
        <i:scalarref identifier="A" ref="inputs.x"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:vectorfromscalar>

```

## decomposevector

**Description:** Node for decomposing a vector into 3 scalar values. The input must have the identifier "A", and the outputs must have the identifiers x, y, and z.

**Inputs:**

| Identifier | Description            | Type      |
|------------|------------------------|-----------|
| A          | Vector to decompose    | vector    |

**Outputs:**

| Identifier | Description            | Type     |
|------------|------------------------|----------|
| x          | X-coordinate           | scalar   |
| y          | Y-coordinate           | scalar   |
| z          | Z-coordinate           | scalar   |

**Example Usage:**

```xml

<i:decomposevector>
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector"/>
    </i:in>
    <i:out>
        <i:scalar identifier="x"/>
        <i:scalar identifier="y"/>
        <i:scalar identifier="z"/>
    </i:out>
</i:decomposevector>

```

## composematrix
**Description:** Composes a matrix from 16 scalar values.

**Inputs:**

| Identifier | Description |
|------------|-------------|
| m00        | Scalar value for element (0,0) of the matrix |
| mRC 		 | Scalar value for element (R,C) of the matrix |
| ...		 | ... |
| m33        | Scalar value for element (3,3) of the matrix |

**Outputs:**

| Identifier | Description |
|------------|-------------|
| result     | Composed matrix |

**Example Usage:**

```xml

<i:composematrix identifier="composeMatrix_0" displayname="composed matrix">
	<i:in>
		<i:scalarref identifier="m00" ref="constantM00.value"/>
		<i:scalarref identifier="m01" ref="constantM01.value"/>
		<i:scalarref identifier="m02" ref="constantM02.value"/>
		<i:scalarref identifier="m03" ref="constantM03.value"/>
		<i:scalarref identifier="m10" ref="constantM10.value"/>
		<i:scalarref identifier="m11" ref="constantM11.value"/>
		<i:scalarref identifier="m12" ref="constantM12.value"/>
		<i:scalarref identifier="m13" ref="constantM13.value"/>
		<i:scalarref identifier="m20" ref="constantM20.value"/>
		<i:scalarref identifier="m21" ref="constantM21.value"/>
		<i:scalarref identifier="m22" ref="constantM22.value"/>
		<i:scalarref identifier="m23" ref="constantM23.value"/>
		<i:scalarref identifier="m30" ref="constantM30.value"/>
		<i:scalarref identifier="m31" ref="constantM31.value"/>
		<i:scalarref identifier="m32" ref="constantM32.value"/>
		<i:scalarref identifier="m33" ref="constantM33.value"/>
	</i:in>
	<i:out>
		<i:matrix identifier="result"/>
	</i:out>
</i:composematrix>

```

## matrixfromcolumns

**Description:** Node for composing a matrix from column vectors. The 4th row is set [0,0,0,1]. 

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | First column vector                |
| B      | Second column vector               |
| C      | Third column vector                |
| D      | Fourth column vector               |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| matrix      | Composed matrix               |

The operation can be used for the following types of inputs and outputs:

| A   | B   | C   | D   | result   |
|-----|-----|-----|-----|----------|
|vector|vector|vector|vector|matrix|

**Example Usage:** 
```xml

<i:matrixfromcolumns identifier="matrixfromcolumns" displayname="composed matrix">
    <i:in>
        <i:vectorref identifier="A" ref="vector0.vector"/>
        <i:vectorref identifier="B" ref="vector1.vector"/>
        <i:vectorref identifier="C" ref="vector2.vector"/>
        <i:vectorref identifier="D" ref="vector3.vector"/>
    </i:in>
    <i:out>
        <i:matrix identifier="result"/>
    </i:out>
</i:matrixfromcolumns>

```

## matrixfromrows

**Description:** Node for composing a Matrix from row vectors. The 4th column is set to (0,0,0,1). 

**Inputs:**
| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | First row vector                |
| B      | Second row vector               |
| C      | Third row vector               |
| D      | Fourth row vector               |

**Outputs:**
| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result      | Composed matrix                |

The operation can be used for the following types of inputs and outputs:
| A   | B   | C   | D   | result   | comment   |
|-----|-----|-----|-----|----------|------------|
| vector   | vector   | vector   | vector   | matrix   | Each row vector represents each row in the matrix |

**Example Usage:**

```xml

<i:matrixfromrows identifier="matrixfromrows" displayname="composed vector">
    <i:in>
        <i:vectorref identifier="A" ref="vector0.vector"/>
        <i:vectorref identifier="B" ref="vector1.vector"/>
        <i:vectorref identifier="C" ref="vector2.vector"/>
        <i:vectorref identifier="D" ref="vector3.vector"/>
    </i:in>
    <i:out>
        <i:matrix identifier="result"/>
    </i:out>
</i:matrixfromrows>

```

## multiplication  
**Description:** Performs the multiplication A x B = result. The inputs must have the identifier "A" and "B", and the output must have the identifier "result". All imputs must be of the same type (scalar, vector, matrix).

**Inputs:**  

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | First value to be multiplied                |
| B      | Second value to be multiplied               |

**Outputs:**  

| Identifier   | Description                              |
|--------------|------------------------------------------|
| result      | Result of the multiplication             |

The operation can be used for the following types of inputs and outputs:  

| A         | B        | result       | comment                            |
|-----------|----------|--------------|------------------------------------|
| scalar    | scalar   | scalar       |                                  |
| vector    | vector   | vector       | vector components are multiplied component-wise |
| matrix    | matrix   | matrix       | matrix elements are multiplied component-wise |

**Example Usage:**  

```xml
 
<i:multiplication identifier="multiplication1" displayname="Multiplication 1">
	<i:in>
		<i:scalarref identifier="A" ref="constant1.c1"/>
		<i:scalarref identifier="B" ref="inputs.radius"/>
	</i:in>
	<i:out>
		<i:scalar identifier="result"/>
	</i:out>
</i:multiplication>

```

## subtraction
**Description:** Performs subtracts the inputs "A" and "B" and writes the difference to the output "result".

**Inputs:**

| Identifier | Description                               |
|------------|-------------------------------------------|
| A          | First value to subtract                   |
| B          | Second value to subtract                  |

**Outputs:**

| Identifier | Description                               |
|------------|-------------------------------------------|
| result     | Difference of A and B                      |

The operation can be used for the following types of inputs and outputs:

| A        | B          | result  | comment                                   |
|----------|------------|---------|-------------------------------------------|
| scalar   | scalar     | scalar  |                                           |
| vector   | vector     | vector  | Vector components are subtracted component-wise       |
| matrix   | matrix     | matrix  | Matrix elements are subtracted component-wise |

**Example Usage:**

```xml
 
<i:subtraction identifier="subtraction1" displayname="Subtraction 1">     
    <i:in>         
        <i:scalarref identifier="A" ref="constant1.c1"/>         
        <i:scalarref identifier="B" ref="inputs.radius"/>     
    </i:in>     
    <i:out>         
        <i:scalar identifier="result"/>     
    </i:out> 
</i:subtraction> 

```

## division
**Description:** Performs a division of the inputs "A" and "B" and writes the quotient to the output "result".

**Inputs:**

| Identifier | Description |
|------------|-------------|
| A          | Dividend    |
| B          | Divisor     |

**Outputs:**

| Identifier | Description |
|------------|-------------|
| result     | Quotient    |

The operation can be used for the following types of inputs and outputs:


| A        | B          | result  | comment                                   |
|----------|------------|---------|-------------------------------------------|
| scalar   | scalar     | scalar  |                                           |
| vector   | vector     | vector  | Vector components are divided component-wise       |
| matrix   | matrix     | matrix  | Matrix elements are divided component-wise |

**Example Usage:**

```xml

<i:division identifier="division1" displayname="Division 1">
    <i:in>
        <i:scalarref identifier="A" ref="constant1.c1"/>
        <i:scalarref identifier="B" ref="inputs.radius"/>
    </i:in>
    <i:out>
        <i:scalar identifier="result"/>
    </i:out>
</i:division>

```

## dot

**Description:** Performs a dot product of two vectors "A" and "B" and writes the result to the output "result".

**Inputs:**

| Identifier | Description |
|------------|-------------|
| A          | First vector |
| B          | Second vector |

**Outputs:**

| Identifier | Description |
|------------|-------------|
| result     | Dot product of A and B |

The operation can be used for the following types of inputs and outputs:

| A       | B       | result  | comment                            |
|---------|---------|---------|------------------------------------|
| vector  | vector  | scalar  | dot product of the two vectors     |

**Example Usage:**

```xml

<i:dot identifier="dotproduct1" displayname="Dot Product 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
        <i:vectorref identifier="B" ref="inputs.vector2"/>
    </i:in>
    <i:out>
        <i:scalar identifier="result"/>
    </i:out>
</i:dot>

```

## cross

**Description:** Performs a cross product of the inputs "A" and "B" and writes the result to the output "result".

**Inputs:**

| Identifier | Description |
|------------|-------------|
| A          | First vector |
| B          | Second vector |

**Outputs:**

| Identifier | Description            |
|------------|------------------------|
| result     | Cross product of A and B |

The operation can be used for the following types of inputs and outputs:

| A       | B       | result  | comment                              |
|---------|---------|---------|--------------------------------------|
| vector  | vector  | vector  | cross product of the two vectors      |

**Example Usage:**

```xml

<i:cross identifier="crossproduct1" displayname="Cross Product 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
        <i:vectorref identifier="B" ref="inputs.vector2"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:cross>

```

## matrixvectormultiplication

**Description:** Performs the matrix vector multiplication `A x B = result`. The output must be a vector with the name "result".

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | Matrix                |
| B      | Vector               |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result      | Product of A and B                |

The operation can be used for the following types of inputs and outputs:

| A   | B   | result   | comment   |
|-----|-----|----------|------------|
| matrix   | vector   | vector   | 

**Example Usage:**
```xml

<matrixvectormultiplication identifier="matVec1" displayname="Matrix Vector Multiplication 1">
    <i:in>
        <i:matrixref identifier="A" ref="inputs.matrix1"/>
        <i:vectorref identifier="B" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</matrixvectormultiplication>

```

## transpose 

**Description:** Performs the transpose of a matrix. The input 'A' must be a matrix and the output must be a matrix with the identifier "result".

**Inputs:** 

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | Matrix to be transposed                |

**Outputs:**  

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result      | Transposed matrix                |

The operation can be used for the following types of inputs and outputs:  

| A   | result   | 
|-----|----------|
| matrix   | matrix   |

**Example Usage:**  

```xml

<i:transpose identifier="transpose1" displayname="Transpose 1">
	<i:in>
		<i:matrixref identifier="A" ref="inputs.matrix1"/>
	</i:in>
	<i:out>
		<i:matrix identifier="result"/>
	</i:out>
</i:transpose>

```

## inverse
**Description:** Computes the inverse of a matrix. The input "A" must be a matrix and the output must be a matrix with the identifier "result".

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | Matrix to compute inverse                |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result      | Inverse of matrix A               |

The operation can be used for the following types of inputs and outputs:

| A   | result   | 
|-----|----------|
| matrix   | matrix   |

**Example Usage:**
```xml

<i:inverse identifier="inverse1" displayname="Inverse 1">
    <i:in>
        <i:matrixref identifier="A" ref="inputs.matrix1"/>
    </i:in>
    <i:out>
        <i:matrix identifier="result"/>
    </i:out>
</i:inverse>

```

## sin

**Description:** Computes sin(A) and writes the result to the output "result".

**Inputs:**

| Identifier  | Description                        |
|-------------|------------------------------------|
| A           | Input for sine function            |

**Outputs:**

| Identifier  | Description                        |
|-------------|------------------------------------|
| result      | Result of the sine function        |

The operation can be used for the following types of inputs and outputs:

| A       | result  | comment |
|---------|---------|---------|
| scalar  | scalar  |         |
| vector  | vector  | Sine of each component of the vector |

Example usage:

```xml

<i:sin identifier="sinus1" displayname="Sinus 1">
    <i:in>
        <i:scalarref identifier="A" ref="inputs.scalar1"/>
    </i:in>
    <i:out>
        <i:scalar identifier="result"/>
    </i:out>
</i:sin>

```

## cos

**Description:** Computes cos(A) and writes the result to the output "result".

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | Input for cosine function               |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result       | Cosine of A                |

The operation can be used for the following types of inputs and outputs:

| A       | result    | comment                                   |
|---------|-----------|-------------------------------------------|
| scalar  | scalar    |                                           |
| vector  | vector    | Cosine of each component of the vector     |

**Example Usage:**

```xml

<i:cos identifier="cosinus1" displayname="Cosinus 1">
    <i:in>
        <i:scalarref identifier="A" ref="inputs.scalar1"/>
    </i:in>
    <i:out>
        <i:scalar identifier="result"/>
    </i:out>
</i:cos>

```

## tan

**Description:** Computes tan(A) and writes the result to the output "result".

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | Input value                |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result      | Tangent of A                |

The operation can be used for the following types of inputs and outputs:

| A   | result   |
|-----|----------|
| scalar   | scalar   |
| vector   | Tangent of each component of the vector  |

**Example Usage:**

```xml

<i:tan identifier="tan1" displayname="Tan 1">
    <i:in>
        <i:scalarref identifier="A" ref="inputs.value"/>
    </i:in>
    <i:out>
        <i:scalar identifier="result"/>
    </i:out>
</i:tan>

```

## arcsin

**Description:** Performs an arcsin function with a scalar or vector as output and a scalar or vector input. The input must have the identifier "A", and the output must have the identifier "result".

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A            | Input for the arcsin function               |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result       | Arcsin of the input                         |

The operation can be used for the following types of inputs and outputs:

| A         | result  | comment                               |
|-----------|---------|---------------------------------------|
| scalar    | scalar  |                                       |
| vector    | vector  | Arcsin of each component of the vector |

**Example Usage:**

```xml

<i:arcsin identifier="arcsin1" displayname="Arcsin 1">
    <i:in>
        <i:scalarref identifier="A" ref="inputs.scalar1"/>
    </i:in>
    <i:out>
        <i:scalar identifier="result"/>
    </i:out>
</i:arcsin>

```

## arccos

**Description:** Performs an arctan function with a scalar or vector as input and a scalar or vector as output. The input must have the identifier "A", and the output must have the indentifier "result".

**Inputs:**

| Identifier   | Description                 |
|--------------|-----------------------------|
| A            | Input value                 |

**Outputs:**

| Identifier   | Description                |
|--------------|----------------------------|
| result       | Arccos of A                |

The operation can be used for the following types of inputs and outputs:

| A         | result | comment                      |
|-----------|--------|------------------------------|
| scalar    | scalar | -                            |
| vector    | vector | Arccos of each component of the vector |

**Example Usage:**

```xml

<i:arccos identifier="arccos1" displayname="Arccos 1">
	<i:in>
		<i:vectorref identifier="A" ref="inputs.vector1"/>
	</i:in>
	<i:out>
		<i:vector identifier="result"/>
	</i:out>
</i:arccos>

```

## arctan

**Description:** Performs an arctan function with a scalar or vector as input and a scalar or vector as output. The input must have the identifier "A", and the output must have the identifier "result". 

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| scalarref    | Scalar input                                |
| vectorref    | Vector input                                |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| scalar       | Scalar output                               |
| vector       | Vector output (arctan of each component)    |

The operation can be used for the following types of inputs and outputs:

| A        | result                     | comment                             |
|----------|----------------------------|-------------------------------------|
| scalar   | scalar                     |                                     |
| vector   | vector                     | arctan of each component of the vector |											

**Example Usage:**

```xml

<i:arctan identifier="arctan1" displayname="Arctan 1">
	<i:in>
		<i:vectorref identifier="A" ref="inputs.vector1"/>
	</i:in>
	<i:out>
		<i:vector identifier="result"/>
	</i:out>
</i:arctan>

```

## arctan2

**Description:** Performs the arctangent of the inputs "A" and "B" and writes the result to the output "result". The inputs can be scalar or vector and the output is scalar or vector.

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | First input                |
| B      | Second input               |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result      | Result of the arctan2 operation                |

The operation can be used for the following types of inputs and outputs:

| A   | B   | result   | comment   |
|-----|-----|----------|------------|
| scalar   | scalar   | scalar   |   |
| vector   | vector   | vector   | arctan2 of each component of the vectors |

**Example Usage:**

```xml

<i:arctan2 identifier="arctan21" displayname="Arctan2 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
        <i:vectorref identifier="B" ref="inputs.vector2"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:arctan2>

```

## min

**Description:** Performs a minimum operation on the inputs "A" and "B" and writes the result to the output "result".

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A            | First operand                               |
| B            | Second operand                              |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result       | Minimum value of A and B                     |

The operation can be used for the following types of inputs and outputs:

| A        | B        | result    | comment                                    |
|----------|----------|-----------|--------------------------------------------|
| scalar   | scalar   | scalar    |                                            |
| vector   | vector   | vector    | Minimum value of each component of vectors |
| matrix   | matrix   | matrix    | Minimum value of each component of matrices|

**Example Usage:**

```xml

<i:min identifier="min1" displayname="Min 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
        <i:vectorref identifier="B" ref="inputs.vector2"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:min>

```

## max

**Description:** Performs a max function on the inputs "A" and "B" and writes the result to the output "result".

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | First value               |
| B      | Second value              |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result      | Maximum value of A and B                |

The operation can be used for the following types of inputs and outputs:

| A   | B   | result   | comment   |
|-----|-----|----------|------------|
| scalar   | scalar   | scalar   |        |
| vector   | vector   | vector   | Maximum of each component of the vectors |
| matrix   | matrix   | matrix   | Maximum of each component of the matrices |

**Example Usage:**

```xml

<i:max identifier="max1" displayname="Max 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
        <i:vectorref identifier="B" ref="inputs.vector2"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:max>

```

## abs

**Description:** Performs the absolute value operation on input "A" and writes the result to output "result".

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | Input for absolute value function        |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result      | Result of absolute value operation                |

The operation can be used for the following types of inputs and outputs:

| A   | result   | comment   |
|-----|----------|------------|
| scalar   | scalar   |            |
| vector   | vector   | Absolute value is computed for each component of the vector |
| matrix   | matrix   | Absolute value is computed for each component of the matrix |

**Example Usage:**

```xml

<i:abs identifier="abs1" displayname="Abs 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:abs>

```


## fmod
**Description:** Computes the remainder of the divison of the inputs "A" / "B" and writes the result to the output "result", as known from C++ fmod.
result = A - B * trunc(A/B) 
The result will have the same sign as A.


**Inputs:**
| Identifier   | Description                      |
|--------------|----------------------------------|
| A            | The dividend                     |
| B            | The divisor                      |

**Outputs:**
| Identifier   | Description                   |
|--------------|-------------------------------|
| result       | The remainder of A divided by B|

The operation can be used for the following types of inputs and outputs:
| A         | B         | result  | comment                           |
|-----------|-----------|---------|-----------------------------------|
| scalar    | scalar    | scalar  |                                   |
| vector    | vector    | vector  | modulo operation of each component of the vectors |
| matrix    | matrix    | matrix  | modulo operation of each component of the matrices|

**Example Usage:**
```xml
 
<i:fmod identifier="fmod1" displayname="Fmod 1">
    <i:in>
        <i:scalarref identifier="A" ref="constant1.c1"/>
        <i:scalarref identifier="B" ref="inputs.radius"/>
    </i:in>
    <i:out>
        <i:scalar identifier="result"/>
    </i:out>
</i:fmod>

```

## mod
**Description:** Performs a modulo operation on the inputs "A" and "B" and writes the result to the output "result" as know from GLSL mod. 
result = A - B * floor(A/B)

**Inputs:**
| Identifier   | Description                      |
|--------------|----------------------------------|
| A            | The dividend                     |
| B            | The divisor                      |

**Outputs:**
| Identifier   | Description                   |
|--------------|-------------------------------|
| result       | The remainder of A divided by B|

The operation can be used for the following types of inputs and outputs:
| A         | B         | result  | comment                           |
|-----------|-----------|---------|-----------------------------------|
| scalar    | scalar    | scalar  |                                   |
| vector    | vector    | vector  | modulo operation of each component of the vectors |
| matrix    | matrix    | matrix  | modulo operation of each component of the matrices|

**Example Usage:**
```xml
 
<i:mod identifier="mod1" displayname="mod 1">
    <i:in>
        <i:scalarref identifier="A" ref="constant1.c1"/>
        <i:scalarref identifier="B" ref="inputs.radius"/>
    </i:in>
    <i:out>
        <i:scalar identifier="result"/>
    </i:out>
<i:mod>

```


## pow

**Description:** Performs a power function with the input "A" as the base and "B" as the exponent. The result is written to the output "result".

**Inputs:**

| Identifier   | Description         |
|--------------|---------------------|
| A            | Base of the power    |
| B            | Exponent of the power|

**Outputs:**

| Identifier   | Description         |
|--------------|---------------------|
| result       | Result of the power  |

The operation can be used for the following types of inputs and outputs:

| A       | B       | result  | comment                                    |
|---------|---------|---------|--------------------------------------------|
| scalar  | scalar  | scalar  |                                             |
| vector  | vector  | vector  | Power of each component of the vectors      |
| matrix  | matrix  | matrix  | Power of each component of the matrices     |

**Example Usage:**
```xml

<i:pow identifier="pow1" displayname="Pow 1">
	<i:in>
		<i:vectorref identifier="A" ref="inputs.vector1"/>
		<i:vectorref identifier="B" ref="inputs.vector2"/>
	</i:in>
	<i:out>
		<i:vector identifier="result"/>
	</i:out>
</i:pow>

```

## sqrt

**Description:** Performs the square root operation on the input "A" and writes the result to the output "result".

**Inputs:**
| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | The value to take the square root of                |

**Outputs:**
| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result      | The square root of A               |

The operation can be used for the following types of inputs and outputs:
| A   | result   | comment   |
|-----|----------|------------|
| scalar   | scalar   |  |
| vector   | vector   | square root of each component of the vector |
| matrix   | matrix   | square root of each component of the matrix |

**Example Usage:**
```xml

<i:sqrt identifier="sqrt1" displayname="Sqrt 1">
	<i:in>
		<i:vectorref identifier="A" ref="inputs.vector1"/>
	</i:in>
	<i:out>
		<i:vector identifier="result"/>
	</i:out>
</i:sqrt>

```

## mesh
**Description:** Evaluates the signed distance to a mesh. The input must have the identifier "pos" and must be a vector. The output is a scalar with the identifier "distance". The mesh is assumed to be closed and watertight.

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| pos      | Input vector                |
| mesh      | Resource identifier for the mesh               |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| distance      | Distance to the mesh                |

The operation can be used for the following types of inputs and outputs:

| pos   | mesh   | distance   | comment   |
|-----|-----|----------|------------|
| vector   | -   | scalar   | -  |

**Example Usage:**
```xml

<i:mesh identifier="distanceToMesh1" displayname="Distance to Mesh 1" objectid="1" >
	<i:in>
		<i:vectorref identifier="pos" ref="inputs.pos"/>
	 	<i:resourceref identifier="mesh" ref="reosurceidnode.value"/>
	</i:in>
	<i:out>
		<i:scalar identifier="distance"/>
	</i:out>
</i:mesh>

```

## unsignedmesh
**Description:** Evaluates the unsigned distance to a mesh. The input must have the identifier "pos" and must be a vector. The output is a scalar with the identifier "distance". The mesh does not need to be closed or watertight.

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| pos      | Input vector                |
| mesh      | Resource identifier for the mesh               |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| distance      | Distance to the mesh                |

The operation can be used for the following types of inputs and outputs:

| pos   | mesh   | distance   | comment   |
|-----|-----|----------|------------|
| vector   | -   | scalar   | -  |

**Example Usage:**
```xml

<i:unsignedmesh identifier="UnsignedDistToMesh1" displayname="Unsigned distance to Mesh" objectid="1" >
	<i:in>
		<i:vectorref identifier="pos" ref="inputs.pos"/>
	 	<i:resourceref identifier="mesh" ref="reosurceidnode.value"/>
	</i:in>
	<i:out>
		<i:scalar identifier="distance"/>
	</i:out>
</i:unsignedmesh>

```

## length

**Description:** Calculates the length of the input vector and writes the result to the output "result".

**Inputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| A      | Input Vector                |

**Outputs:**

| Identifier   | Description                                 |
|--------------|---------------------------------------------|
| result      | Length of the input vector                |

The operation can be used for the following types of inputs and outputs:

| A   | result   | comment   |
|-----|----------|------------|
| vector   | scalar   |  length(vector) = scalar  |

**Example Usage:**

```xml

<i:length identifier="length1" displayname="Length 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:scalar identifier="result"/>
    </i:out>
</i:length>

```

## log

**Description:** Performs a natural logarithm of the input "A" and writes the result to the output "result". 

**Inputs:**

| Identifier   | Description                              |
|--------------|------------------------------------------|
| A            | Value to compute natural logarithm for    |

**Outputs:**

| Identifier   | Description                             |
|--------------|-----------------------------------------|
| result       | Natural logarithm of input "A"           |

The operation can be used for the following types of inputs and outputs:

| A         | result   | comment                                 |
|-----------|----------|-----------------------------------------|
| scalar    | scalar   |                                         |
| vector    | vector   | Natural logarithm of each component     |
| matrix    | matrix   | Natural logarithm of each component     |

**Example Usage:**

```xml

<i:log identifier="log_1" displayname="Log_n 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:log>

```

## log2 

**Description:** Performs a base 2 logarithm operation on the input "A" and writes the result to the output "result".

**Inputs:**

| Identifier | Description |
|------------|-------------|
| A          | Value to calculate logarithm of |

**Outputs:**

| Identifier | Description |
|------------|-------------|
| result     | Result of the logarithm calculation |

The operation can be used for the following types of inputs and outputs:

| A      | result   | comment                             |
|--------|----------|-------------------------------------|
| scalar | scalar   |                                     |
| vector | vector   | Logarithm is calculated componentwise |
| matrix | matrix   | Logarithm is calculated componentwise |

**Example Usage:**

```xml

<i:log2 identifier="log21" displayname="Log2 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:log2>

```

## log10
**Description:** Performs a base 10 logarithm of the input "A" and writes the result to the output "result".

**Inputs:**
| Identifier | Description |
|------------|-------------|
| A          | Number to calculate the logarithm of |

**Outputs:**
| Identifier | Description                          |
|------------|--------------------------------------|
| result     | Base 10 logarithm of input number A   |

The operation can be used for the following types of inputs and outputs:
| A       | result  | comment                               |
|---------|---------|---------------------------------------|
| scalar  | scalar  |                                       |
| vector  | vector  | Logarithm is calculated componentwise |
| matrix  | matrix  | Logarithm is calculated componentwise |

**Example Usage:**
```xml

<i:log10 identifier="log101" displayname="Log10 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:log10>

```

## exp
**Description:** Performs an exponential function on the input "A" and writes the result to the output "result".

**Inputs:**
| Identifier | Description              |
|------------|--------------------------|
| A          | Input for exponential function |

**Outputs:**
| Identifier | Description              |
|------------|--------------------------|
| result     | Result of exponential function | 

The operation can be used for the following types of inputs and outputs:
| A      | result  | Comment                          |
|--------|---------|----------------------------------|
| scalar | scalar  |                                  | 
| vector | vector  | Exponential of each component of the vector |
| matrix | matrix  | Exponential of each component of the matrix | 

**Example Usage:**
```xml

<i:exp identifier="exp1" displayname="Exp 1">
	<i:in>
		<i:vectorref identifier="A" ref="inputs.vector1"/>
	</i:in>
	<i:out>
		<i:vector identifier="result"/>
	</i:out>
</i:exp>

```

## cosh

**Description:** Performs a hyperbolic cosine function on the input "A" and writes the result to the output "result".

**Inputs:**

| Identifier | Description                                 |
|------------|---------------------------------------------|
| A          | Input value for the hyperbolic cosine function |

**Outputs:**

| Identifier | Description                                 |
|------------|---------------------------------------------|
| result     | Result of the hyperbolic cosine function     |

The operation can be used for the following types of inputs and outputs:

| A       | result     | comment                              |
|---------|------------|--------------------------------------|
| scalar  | scalar     |                                      |
| vector  | vector     | cosh of each component of the vector |
| matrix  | matrix     | cosh of each component of the matrix |

**Example Usage:**

```xml

<i:cosh identifier="cosh1" displayname="Cosh 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:cosh>

```

## sinh

**Description:** Calculates the hyperbolic sine of the input "A" and writes the result to the output "result".

**Inputs:**

| Identifier | Description | 
|------------|-------------|
| A          | Operand     |

**Outputs:**

| Identifier | Description |
|------------|-------------|
| result     | Result      |

The operation can be used for the following types of inputs and outputs:

| A       | result  | comment                              |
|---------|---------|--------------------------------------|
| scalar  | scalar  |                                      |
| vector  | vector  | sinh of each component of the vector  |
| matrix  | matrix  | sinh of each component of the matrix  |

**Example Usage:**

```xml

<i:sinh identifier="sinh1" displayname="Sinh 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:sinh>

```

## tanh

**Description:** Calculates the hyperbolic tangent of the input "A" and writes the result to the output "result".

**Inputs:**

| Identifier | Description |
|------------|-------------|
| A          | Operand     |

**Outputs:**

| Identifier | Description |
|------------|-------------|
| result     | Result      |

The operation can be used for the following types of inputs and outputs:

| A       | result  | comment                              |
|---------|---------|--------------------------------------|
| scalar  | scalar  |                                      |
| vector  | vector  | tanh of each component of the vector  |
| matrix  | matrix  | tanh of each component of the matrix  |

**Example Usage:**

```xml

<i:tanh identifier="tanh1" displayname="Tanh 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:tanh>

```

## clamp

**Description:** Performs the clamp function `max(min, min(A,max))`. The input must have the identifier "A" (value), "min", and "max". The output must have the identifier "result".

**Inputs:**

| Identifier | Description                |
|------------|----------------------------|
| A          | Value                      |
| min        | Minimum value              |
| max        | Maximum value              |

**Outputs:**

| Identifier | Description                |
|------------|----------------------------|
| result     | Result of the clamp function|

The operation can be used for the following types of inputs and outputs:

| A       | min     | max     | result                     | 
|---------|---------|---------|----------------------------|
| scalar  | scalar  | scalar  | scalar                     | 
| vector  | vector  | vector  | Vector with clamped values component-wise |
| matrix  | matrix  | matrix  | Matrix with clamped values component-wise |

**Example Usage:**

```xml

<i:clamp identifier="clamp1" displayname="Clamp 1">
    <i:in>
        <i:scalarref identifier="A" ref="inputs.scalar1"/>
        <i:scalarref identifier="min" ref="inputs.scalar2"/>
        <i:scalarref identifier="max" ref="inputs.scalar3"/>
    </i:in>
    <i:out>
        <i:scalar identifier="result"/>
    </i:out>
</i:clamp>

```

## select

**Description:** Derived node for a select function. The input must have the identifier "A", "B", "C", "D", and the output must have the identifier "result". If A < B then the result is C, otherwise D.

**Inputs:**

| Identifier  | Description                      |
|-------------|----------------------------------|
| A           | First value to compare           |
| B           | Second value to compare          |
| C           | Result if A < B                  |
| D           | Result if A >= B                 |

**Outputs:**

| Identifier | Description                      |
|------------|----------------------------------|
| result     | Result of A < B ? C : D          |

The operation can be used for the following types of inputs and outputs:

| A       | B       | C       | D       | result      |
|---------|---------|---------|---------|-------------|
| scalar  | scalar  | scalar  | scalar  | scalar      |
| vector  | vector  | vector  | vector  | vector      |
| matrix  | matrix  | matrix  | matrix  | matrix      |

**Example Usage:**
```xml

<i:select identifier="select1" displayname="Select 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
        <i:vectorref identifier="B" ref="inputs.vector2"/>
        <i:vectorref identifier="C" ref="inputs.vector3"/>
        <i:vectorref identifier="D" ref="inputs.vector4"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:select>

```

## round

**Description:** Performs a rounding operation on the input "A" and writes the result to the output "result".

**Inputs:**

| Identifier | Description |
| --- | --- |
| A | Value to be rounded |

**Outputs:**

| Identifier | Description |
| --- | --- |
| result | Rounded value of A |

The operation can be used for the following types of inputs and outputs:

| A | result | comment |
| --- | --- | --- |
| scalar | scalar |  |
| vector | vector | Round of each component of the vector |
| matrix | matrix | Round of each component of the matrix |

**Example Usage:**

```xml

<i:round identifier="round1" displayname="Round 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:round>

```

## ceil

**Description:** Performs the ceil function on the input "A" and writes the result to the output "result".

**Inputs:**

| Identifier   | Description                           |
|--------------|---------------------------------------|
| A            | Value to be rounded up                |

**Outputs:**

| Identifier   | Description                           |
|--------------|---------------------------------------|
| result       | Rounded up value                       |

The operation can be used for the following types of inputs and outputs:

| A          | result        | comment                                  |
|------------|---------------|------------------------------------------|
| scalar     | scalar        | Round up a single scalar value            |
| vector     | vector        | Round up each component of the vector     |
| matrix     | matrix        | Round up each component of the matrix     |

**Example Usage:**

```xml

<i:ceil identifier="ceil1" displayname="Ceil 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:ceil>

```

## floor

**Description:** Performs a floor function on the input "A" and writes the result to the output "result".

**Inputs:**

| Identifier | Description |
|------------|-------------|
| A          | Value to be rounded down |

**Outputs:**

| Identifier | Description     |
|------------|-----------------|
| result     | Rounded down value of A |

The operation can be used for the following types of inputs and outputs:

| A       | result  | comment                             |
|---------|---------|-------------------------------------|
| scalar  | scalar  |                                     |
| vector  | vector  | Floor of each component of the vector |
| matrix  | matrix  | Floor of each component of the matrix|

**Example Usage:**

```xml

<i:floor identifier="floor1" displayname="Floor 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:floor>

```
## sign

**Description:** Performs the sign function on the input "A" and writes the result to the output "result". If the input is less than zero this function returns -1, if the input is greater than zero this function returns 1, and if the input is equal to zero this function returns 0.

**Inputs:**

| Identifier | Description |
| --- | --- |
| A | Input value |

**Outputs:**

| Identifier | Description |
| --- | --- |
| result | Sign of the input |

The operation can be used for the following types of inputs and outputs:

| A | result | comment |
| --- | --- | --- |
| scalar | scalar |  |
| vector | vector | Sign of each component of the vector |
| matrix | matrix | Sign of each component of the matrix |

**Example Usage:**

```xml

<i:sign identifier="sign1" displayname="Sign 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:sign>

```

## fract
**Description:** Returns the fractional part of the input (A - floor(A)).

**Inputs:**

| Identifier | Description |
|------------|-------------|
| A          | Input value |

**Outputs:**

| Identifier | Description |
|------------|-------------|
| result     | Fractional part of A |

The operation can be used for the following types of inputs and outputs:

| A       | result | Comment                                     |
|---------|--------|---------------------------------------------|
| scalar  | scalar |                                              |
| vector  | vector | Sign of each component of the vector         |
| matrix  | matrix | Sign of each component of the matrix         |

**Example Usage:**

```xml

<i:sign identifier="sign1" displayname="Sign 1">
    <i:in>
        <i:vectorref identifier="A" ref="inputs.vector1"/>
    </i:in>
    <i:out>
        <i:vector identifier="result"/>
    </i:out>
</i:sign>

```

## functionCall
**Description:** Calls a function with the given identifier. The input must have the identifier "functionID". The rest of the inputs and outputs must match the inputs and outputs of the function.

**Inputs:**

| Identifier | Description |
|------------|-------------|
| functionID | Identifier of the function to call |
| defined by function | |

**Outputs:**

| Identifier | Description |
|------------|-------------|
| defined by function | |

**Example Usage:**

```xml

<i:functioncall identifier="functionCall1" displayname="Function Call 1">
	<i:in>
		<i:resourceref identifier="functionID" ref="resourceidnode.value"/>
	</i:in>
	<i:out>
		<i:scalar identifier="result"/>
	</i:out>
</i:functioncall>

```

Calling the sphere function from the example in [Chapter 2. Function Implicit](#chapter-2-function-implicit) could look like this:

```xml
    <i:constant identifier="ConstantScalar_3" displayname="Radius" tag="" value="10">
        <i:out>
            <i:scalar identifier="value" displayname="value"></i:scalar>
        </i:out>
    </i:constant>
    <i:constresourceid identifier="FunctionCall_5_functionID" displayname="sphere_functionID" tag="" resourceid="5">
        <i:out>
            <i:resourceid identifier="value" displayname="value"></i:resourceid>
        </i:out>
    </i:constresourceid>
    <i:functioncall identifier="FunctionCall_6" displayname="sphere" tag="">
        <i:in>
            <i:resourceref identifier="functionID" displayname="functionID" ref="FunctionCall_5_functionID.value"></i:resourceref>
            <i:vectorref identifier="pos" displayname="pos" ref="Subtraction_5.result"></i:vectorref>
            <i:scalarref identifier="radius" displayname="radius" ref="ConstantScalar_3.value"></i:scalarref>
        </i:in>
        <i:out>
            <i:scalar identifier="shape" displayname="shape"></i:scalar>
        </i:out>
    </i:functioncall>
```
The inputs of the sphere function are added as inputs to the `<i:functioncall>` node. The output of the  `<i:functioncall>` node is the output of the sphere function. A `<i:constresourceid>` node is used to define the functionID of the sphere function. Note that a resourceid can also be used as a function input.

## Chapter 5. Implicit Evaluation

## 5.1 Valid Graphs

The native nodes provided are used to create abitrary graphs. In order for these graphs to be evaluatable they must meet the following criteria and any graph that fails to meet this criteria MUST be rejected.
- Nodes that compose a Function form a subgraph that must be acyclic and directed.
- References between Functions that form the graph MUST be acyclic and directed.
- A Function MUST NOT reference itself.
- Inputs must only reference outputs of the same DataType.

## 5.2 Undefined Results and Fallback Values

The native nodes provided can create graphs that have regions that will evaluate to an undefined value. This undefined value presents a problem when trying to evaluate a <levelset> object or a a volume data element such as <color>. Such undefined results make the result of the function undefined and the volumetric data element MUST be evaluated to the volumetric data element's fallback value.

## Chapter 6. Notes


# Part III. Appendices

# Appendix A. Glossary

See [the standard 3MF Glossary](https://github.com/3MFConsortium/spec_resources/blob/master/glossary.md).

## Appendix B. 3MF XSD Schema for the Volumetric and Implicit Extensions
VOLUMETRIC_SCHEMA_INSERT

_sheet0.png_
![sheet0.png](images/sheet0.png)

IMPLICIT_SCHEMA_INSERT

_sheet1.png_
![sheet1.png](images/sheet1.png)


# References

[1] Pasko, Alexander, et al. "Function representation in geometric modeling: concepts, implementation and applications." The visual computer 11.8 (1995): 429-446.

[2] Wyvill, Brian, Andrew Guy, and Eric Galin. "Extending the csg tree. warping, blending and boolean operations in an implicit surface modeling system." Computer Graphics Forum. Vol. 18. No. 2. Oxford, UK and Boston, USA: Blackwell Publishers Ltd, 1999.

See also [the standard 3MF References](https://github.com/3MFConsortium/spec_resources/blob/master/references.md).

Copyright 3MF Consortium 2024.
